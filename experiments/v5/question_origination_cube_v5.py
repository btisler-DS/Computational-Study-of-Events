#!/usr/bin/env python3
"""Question-origination experiment V5: projected 3D cube with three observers, adjustable duration and speed.

Only spatial geometry changes from V2: particles and D use (x,y,z),
(vx,vy,vz); walls are the six faces of a 380-unit cube; collision tests
and spawning use three-dimensional distances and directions. All other
rules, identities, caps, colors, trailing perspectives and observer encounter
records are maintained. D's encounters are computational access events;
they do not establish whether a question was asked. V1/V2 are not modified.

Dependencies: Python 3.9+, numpy, opencv-python, ffmpeg (optional H264).
Usage: python question_origination_cube_v5.py --output cube_v3.mp4
       python question_origination_cube_v5.py --no-video --event-log events.json
"""
from __future__ import annotations
import argparse
import json
import math
import os
import random
import shutil
import subprocess
from dataclasses import dataclass
from pathlib import Path

import cv2
import numpy as np

FPS=30
ARENA=380
NORMAL_R=10.0
SMALL_R=5.5
OBSERVER_R=10.5
MAX_BALLS=88
GREEN=(72,215,90)
BLUE=(250,155,55)
RED=(80,75,242)
YELLOW=(72,215,250)
CYAN=(255,232,38)
OBS1=(225,112,160)
OBS2=(40,170,255)
OBS3=(235,240,245)
WHITE=(235,240,245)
MUTED=(161,174,190)
BACKGROUND=(12,15,24)
PANEL=(23,28,41)
WIDTH, HEIGHT=1590,790
VIEW_SIDE=490
LEFT=(32,161)
RIGHT=(553,161)
CENTER=ARENA/2
YAW=math.radians(36)
ELEV=math.radians(25)
SCALE=.78
# Axonometric basis for X (screen right), Y (screen down) and Z (depth).
# y positive down in screen coordinates, consistent with V2's y coordinate.

def project(x,y,z):
    xx=x-CENTER; yy=y-CENTER; zz=z-CENTER
    u=(xx*math.cos(YAW)-zz*math.sin(YAW))*SCALE
    v=(yy*math.cos(ELEV)+(xx*math.sin(YAW)+zz*math.cos(YAW))*math.sin(ELEV))*SCALE
    return (int(round(VIEW_SIDE/2+u)),int(round(VIEW_SIDE/2+v)))

@dataclass
class Ball:
    ident:int
    x:float
    y:float
    z:float
    vx:float
    vy:float
    vz:float
    r:float
    born:int
    grow:bool=False
    fixed:bool=False
    label:str=''
    prev:tuple|None=None
    def color(self):
        if self.ident==0:return GREEN
        if self.ident==1:return BLUE
        if self.grow:return YELLOW
        return RED

@dataclass
class Observer:
    ident:str
    color:tuple
    x:float=337.0
    y:float=333.0
    z:float=337.0
    vx:float=0.0
    vy:float=0.0
    vz:float=0.0
    r:float=OBSERVER_R
    active:bool=False
    contacted:bool=False
    last_event:int=-9999
    prev:tuple|None=None

def txt(img,s,pos,scale=.53,color=WHITE,thickness=1):
    cv2.putText(img,str(s),tuple(map(int,pos)),cv2.FONT_HERSHEY_SIMPLEX,scale,color,thickness,cv2.LINE_AA)

def unit_3d(rng):
    """Uniformly oriented 3D direction instead of V2's planar angle."""
    az=rng.uniform(0,2*math.pi)
    zz=rng.uniform(-1,1)
    horizontal=math.sqrt(max(0,1-zz*zz))
    return horizontal*math.cos(az),horizontal*math.sin(az),zz

def advance_observer(d,c,frame,dt,speed_scale=1.0):
    """Same pursuit/retreat as V2, extended to three spatial components."""
    d.prev=(d.x,d.y,d.z)
    if c is None:return
    d.active=True
    dx,dy,dz=c.x-d.x,c.y-d.y,c.z-d.z
    norm=max(math.sqrt(dx*dx+dy*dy+dz*dz),.001)
    if frame-d.last_event<round(.8*FPS):
        speed=-156.0*speed_scale
    else:
        speed=205.0*speed_scale
    f=.22
    d.vx=(1-f)*d.vx+f*dx/norm*speed
    d.vy=(1-f)*d.vy+f*dy/norm*speed
    d.vz=(1-f)*d.vz+f*dz/norm*speed
    for axis in ('x','y','z'):
        pos=getattr(d,axis)+getattr(d,'v'+axis)*dt
        vel=getattr(d,'v'+axis)
        if pos<d.r:pos=2*d.r-pos;vel=abs(vel)
        if pos>ARENA-d.r:pos=2*(ARENA-d.r)-pos;vel=-abs(vel)
        setattr(d,axis,pos);setattr(d,'v'+axis,vel)

def draw_cube(img,off):
    vertices={i:project(*xyz) for i,xyz in enumerate((
        (0,0,0),(ARENA,0,0),(0,ARENA,0),(ARENA,ARENA,0),
        (0,0,ARENA),(ARENA,0,ARENA),(0,ARENA,ARENA),(ARENA,ARENA,ARENA)))}
    for i in range(8):
        for bit in (1,2,4):
            j=i^bit
            if j<i:continue
            a=vertices[i];b=vertices[j]
            start=(off[0]+a[0],off[1]+a[1]);end=(off[0]+b[0],off[1]+b[1])
            # Rear edges subdued, keeping spatial geometry visually legible.
            color=(58,69,82) if (i&4)==0 and (j&4)==0 else (93,112,135)
            cv2.line(img,start,end,color,1,cv2.LINE_AA)
    # Explicit X/Y/Z coordinate vectors from the far-front corner.
    base=project(0,0,0)
    axes=[('X',project(ARENA*.35,0,0),(90,155,230)),
          ('Y',project(0,ARENA*.35,0),(116,218,161)),
          ('Z',project(0,0,ARENA*.35),(190,127,226))]
    p=(off[0]+base[0],off[1]+base[1])
    for name,tip,color in axes:
        q=(off[0]+tip[0],off[1]+tip[1])
        cv2.arrowedLine(img,p,q,color,2,cv2.LINE_AA,tipLength=.15)
        txt(img,name,(q[0]+5,q[1]-5),.46,color,1)

def draw_sphere(img,x,y,rad,color):
    # 3D projected orthographically; circle size is fixed for equal radius.
    cv2.circle(img,(x,y),max(2,int(round(rad*SCALE+2))),(23,28,37),-1,cv2.LINE_AA)
    cv2.circle(img,(x,y),max(2,int(round(rad*SCALE))),color,-1,cv2.LINE_AA)
    cv2.circle(img,(x-2,y-2),max(1,int(round(rad*SCALE*.24))),(235,235,235),-1,cv2.LINE_AA)

def render_cube_frame(img,off,layer,balls,observers,event_log,c_origin,frame):
    x,y=off
    img[y:y+VIEW_SIDE,x:x+VIEW_SIDE]=layer
    draw_cube(img,off)
    cv2.rectangle(img,(x-1,y-1),(x+VIEW_SIDE,y+VIEW_SIDE),(64,77,96),1)
    # Historical markers represent encounter position, never physical forcing.
    for ev in event_log[-4:]:
        age=(frame-ev['frame'])/FPS
        if 0<=age<=2.1:
            p=ev['where'];u,v=project(p['x'],p['y'],p['z'])
            rad=int(10+age*24)
            cv2.circle(img,(x+u,y+v),rad,CYAN,2,cv2.LINE_AA)
            txt(img,ev['question_id'],(x+u+12,y+v-12),.40,CYAN)
    if event_log and c_origin:
        ev=event_log[-1]
        if 0<=(frame-ev['frame'])/FPS<=3.0:
            start=c_origin['collision_location'];end=ev['where']
            a=project(start['x'],start['y'],start['z'])
            b=project(end['x'],end['y'],end['z'])
            a=(x+a[0],y+a[1]);b=(x+b[0],y+b[1])
            n=max(1,int(math.dist(a,b)/11))
            for i in range(0,n,2):
                t=i/n;u=min(1,(i+1)/n)
                aa=(int(a[0]*(1-t)+b[0]*t),int(a[1]*(1-t)+b[1]*t))
                bb=(int(a[0]*(1-u)+b[0]*u),int(a[1]*(1-u)+b[1]*u))
                cv2.line(img,aa,bb,CYAN,1,cv2.LINE_AA)
            cv2.circle(img,a,7,CYAN,1,cv2.LINE_AA)
    # Approximate visibility for opaque projected spheres via depth ordering.
    objects=[((b.x*math.sin(YAW)-b.z*math.cos(YAW))*math.cos(ELEV)-b.y*math.sin(ELEV),b) for b in balls]
    objects.extend([((d.x*math.sin(YAW)-d.z*math.cos(YAW))*math.cos(ELEV)-d.y*math.sin(ELEV),d) for d in observers])
    objects.sort(key=lambda t:t[0])
    for _,obj in objects:
        u,v=project(obj.x,obj.y,obj.z)
        color=obj.color if isinstance(obj,Observer) else obj.color()
        draw_sphere(img,x+u,y+v,obj.r,color)
        if isinstance(obj,Observer):
            txt(img,obj.ident,(x+u+10,y+v-10),.41,WHITE)
        elif obj.ident<=2:
            txt(img,obj.label,(x+u+10,y+v-10),.43,WHITE)

def generate(output='question_origination_cube_v5.mp4',seconds=60.0,seed=14,
             log_path=None,no_video=False,capture_times=None,speed_scale=0.5):
    rng=random.Random(seed)
    # V2 initial positions/velocities, with an added shared Z coordinate.
    # They still make the first A-B encounter; all later births can move in Z.
    balls=[Ball(0,95,177,190,93*speed_scale,21*speed_scale,0,NORMAL_R,0,True,True,'A'),
           Ball(1,283,177,190,-91*speed_scale,21*speed_scale,0,NORMAL_R,0,True,True,'B')]
    observers=[Observer('D1',OBS1,337.0,333.0,337.0),
               Observer('D2',OBS2,43.0,333.0,337.0),
               Observer('D3',OBS3,337.0,47.0,43.0)]
    next_id=2
    births=0;growths=0;collision_count=0
    contact_ages={}
    permanent=np.full((VIEW_SIDE,VIEW_SIDE,3),BACKGROUND,dtype=np.uint8)
    fade_secondary=permanent.copy()
    permanent_original=permanent.copy()
    dark=np.array(BACKGROUND,dtype=np.float32)
    first_collision=None;c_origin=None
    birth_events=[];growth_events=[];progress=[];question_events=[]
    dt=1/FPS;frames=round(seconds*FPS)
    output=Path(output)
    video=None
    if not no_video:
        output.parent.mkdir(parents=True,exist_ok=True)
        temp=output.with_name(output.stem+'_raw.mp4')
        video=cv2.VideoWriter(str(temp),cv2.VideoWriter_fourcc(*'mp4v'),FPS,(WIDTH,HEIGHT))
        if not video.isOpened():raise RuntimeError('Unable to initialize MP4 writer')
    capture_times=capture_times or []
    capture_at=set(min(frames-1,max(0,round(t*FPS))) for t in capture_times)
    captures=[]
    for frame in range(frames):
        # V2 mechanics are identical, expressed over x/y/z and 3D distances.
        for b in balls:
            b.prev=(b.x,b.y,b.z,b.color())
            for axis in ('x','y','z'):
                pos=getattr(b,axis)+getattr(b,'v'+axis)*dt
                vel=getattr(b,'v'+axis)
                if pos<b.r:pos=2*b.r-pos;vel=abs(vel)
                if pos>ARENA-b.r:pos=2*(ARENA-b.r)-pos;vel=-abs(vel)
                setattr(b,axis,pos);setattr(b,'v'+axis,vel)
        spawned=[]
        for i in range(len(balls)):
            a=balls[i]
            for j in range(i+1,len(balls)):
                b=balls[j]
                dx=b.x-a.x;dy=b.y-a.y;dz=b.z-a.z
                dsq=dx*dx+dy*dy+dz*dz
                rr=a.r+b.r
                if dsq>=rr*rr:continue
                dist=max(math.sqrt(dsq),.001)
                nx,ny,nz=dx/dist,dy/dist,dz/dist
                rel=(b.vx-a.vx)*nx+(b.vy-a.vy)*ny+(b.vz-a.vz)*nz
                overlap=rr-dist
                a.x-=nx*overlap*.51;a.y-=ny*overlap*.51;a.z-=nz*overlap*.51
                b.x+=nx*overlap*.51;b.y+=ny*overlap*.51;b.z+=nz*overlap*.51
                if rel<0:
                    a.vx+=rel*nx;a.vy+=rel*ny;a.vz+=rel*nz
                    b.vx-=rel*nx;b.vy-=rel*ny;b.vz-=rel*nz
                key=(a.ident,b.ident)
                if frame-contact_ages.get(key,-999)>9 and rel<0:
                    contact_ages[key]=frame
                    collision_count+=1
                    for participant in (a,b):
                        if not participant.grow:
                            participant.r=NORMAL_R
                            participant.grow=True
                            growths+=1
                            growth_events.append({'frame':frame,'time_seconds':round(frame/FPS,5),'ball_id':participant.ident})
                    if len(balls)+len(spawned)<MAX_BALLS:
                        mx=(a.x+b.x)/2;my=(a.y+b.y)/2;mz=(a.z+b.z)/2
                        proposed=None
                        # Same up-to-20 collision-free placement attempts,
                        # but rotate candidates in 3D, not a 2D plane.
                        ux,uy,uz=unit_3d(rng)
                        for k in range(20):
                            if k>0:ux,uy,uz=unit_3d(rng)
                            sr=SMALL_R
                            px=min(max(mx+ux*26,sr+2),ARENA-sr-2)
                            py=min(max(my+uy*26,sr+2),ARENA-sr-2)
                            pz=min(max(mz+uz*26,sr+2),ARENA-sr-2)
                            if all((px-t.x)**2+(py-t.y)**2+(pz-t.z)**2>(sr+t.r+1)**2 for t in balls+spawned):
                                proposed=(px,py,pz,ux,uy,uz);break
                        if proposed is not None:
                            px,py,pz,ux,uy,uz=proposed
                            speed=rng.uniform(90,155)*speed_scale
                            born=Ball(next_id,px,py,pz,ux*speed,uy*speed,uz*speed,sr,frame,False,next_id==2,'C' if next_id==2 else '')
                            spawned.append(born)
                            be={'frame':frame,'time_seconds':round(frame/FPS,5),'parents':[a.ident,b.ident],
                                'child':next_id,'location':{'x':round(px,5),'y':round(py,5),'z':round(pz,5)},
                                'collision_location':{'x':round(mx,5),'y':round(my,5),'z':round(mz,5)}}
                            birth_events.append(be)
                            if next_id==2:c_origin=be
                            next_id+=1;births+=1
                    if first_collision is None:
                        first_collision={'frame':frame,'time_seconds':round(frame/FPS,5),'participants':[a.ident,b.ident]}
        balls.extend(spawned)
        c=balls[2] if len(balls)>2 and balls[2].ident==2 else None
        for d in observers:
            advance_observer(d,c,frame,dt,speed_scale)
        if c is not None:
            for d in observers:
                dist=math.sqrt((d.x-c.x)**2+(d.y-c.y)**2+(d.z-c.z)**2)
                touching=dist<=d.r+c.r
                if touching and not d.contacted and frame-d.last_event>=round(.9*FPS):
                    d.last_event=frame
                    qnum=len(question_events)+1
                    ev={
                        'question_id':f'Q{qnum}',
                        'observer':d.ident,'potential_id':'C',
                        'frame':frame,'time_seconds':round(frame/FPS,5),
                        'c_state_at_encounter':'grown_yellow' if c.grow else 'small_red',
                        'where':{'x':round(c.x,5),'y':round(c.y,5),'z':round(c.z,5)},
                        'interrogatives':{
                            'WHO':f'observer {d.ident} encountered potential C',
                            'WHAT':'C state '+('grown/yellow' if c.grow else 'small/red'),
                            'WHERE':f'C at x={c.x:.2f}, y={c.y:.2f}, z={c.z:.2f}',
                            'WHEN':f't={frame/FPS:.3f}s, frame={frame}',
                            'HOW':'trace C (id=2) birth from original collision A+B',
                            'WHY':'unresolved; question content is not simulated',
                        },
                        'c_lineage':{
                            'original_collision':c_origin,
                            'subsequent_growth':[ge for ge in growth_events if ge['ball_id']==2 and ge['frame']<=frame],
                        },
                        'event_kind':'observer_potential_access',
                    }
                    question_events.append(ev)
                d.contacted=touching
        # Same two views and original A/B/C trail retention as V2.
        fade_secondary=((fade_secondary.astype(np.float32)-dark)*.953+dark).astype(np.uint8)
        for b in balls:
            if b.prev is None:continue
            x0,y0,z0,c0=b.prev
            p1=project(x0,y0,z0);p2=project(b.x,b.y,b.z)
            original=b.ident<=2
            cv2.line(permanent,p1,p2,b.color(),2 if original else 1,cv2.LINE_AA)
            if original:cv2.line(permanent_original,p1,p2,b.color(),2,cv2.LINE_AA)
            if not original:cv2.line(fade_secondary,p1,p2,b.color(),2,cv2.LINE_AA)
        if video is not None or frame in capture_at:
            bg=np.full_like(fade_secondary,BACKGROUND)
            mask=np.any(permanent_original!=bg,axis=2)
            fading=fade_secondary.copy()
            fading[mask]=permanent_original[mask]
            canvas=np.full((HEIGHT,WIDTH,3),BACKGROUND,dtype=np.uint8)
            txt(canvas,'QUESTION POTENTIAL   /   3D CUBE EXPERIMENT V5',(34,48),.79,WHITE,2)
            txt(canvas,'V4 rules with adjustable duration and speed',(34,74),.52,MUTED)
            for off,layer,heading in ((LEFT,permanent,'PERSISTENT HISTORY'),(RIGHT,fading,'FADING SECONDARY HISTORY')):
                txt(canvas,heading,(off[0],off[1]-18),.59,WHITE)
                render_cube_frame(canvas,off,layer,balls,observers,question_events,c_origin,frame)
            sx=1083
            cv2.rectangle(canvas,(sx,123),(1570,653),PANEL,-1)
            cv2.rectangle(canvas,(sx,123),(1570,653),(70,85,106),1)
            txt(canvas,'D1 D2 D3   /   OBSERVERS',(sx+20,154),.65,WHITE,2)
            txt(canvas,'All three encounter original C only',(sx+20,182),.49,MUTED)
            cv2.circle(canvas,(sx+26,205),6,OBS1,-1,cv2.LINE_AA); txt(canvas,'D1', (sx+40,211), .44, WHITE)
            cv2.circle(canvas,(sx+95,205),6,OBS2,-1,cv2.LINE_AA); txt(canvas,'D2', (sx+109,211), .44, WHITE)
            cv2.circle(canvas,(sx+164,205),6,OBS3,-1,cv2.LINE_AA); txt(canvas,'D3', (sx+178,211), .44, WHITE)
            txt(canvas,'Encounter records: '+str(len(question_events)),(sx+20,236),.59,WHITE)
            txt(canvas,'X, Y, Z   /   all positions in cube units',(sx+20,267),.47,MUTED)
            txt(canvas,f'Speed scale   {speed_scale:.2f}x',(sx+20,289),.47,MUTED)
            txt(canvas,f'Duration target   {seconds:.0f}s',(sx+20,311),.47,MUTED)
            if c_origin:
                txt(canvas,'C <- first A+B collision',(sx+20,338),.55,YELLOW)
                txt(canvas,f"C birth   t={c_origin['time_seconds']:.2f}s",(sx+20,365),.48,MUTED)
            else:
                txt(canvas,'Awaiting first A+B collision',(sx+20,338),.49,MUTED)
            if question_events:
                ev=question_events[-1]
                txt(canvas,f"{ev['question_id']} {ev['observer']} / {ev['c_state_at_encounter'].replace('_',' ')}",(sx+20,398),.53,CYAN,2)
                for i,k in enumerate(('WHO','WHAT','WHERE','WHEN','HOW','WHY')):
                    y=431+i*31
                    txt(canvas,k,(sx+20,y),.45,(178,198,219))
                    if k=='WHO':v=f"{ev['observer']} encounters C"
                    elif k=='WHAT':v=ev['c_state_at_encounter'].replace('_',' ')
                    elif k=='WHERE':
                        p=ev['where'];v=f"x={p['x']:.1f} y={p['y']:.1f} z={p['z']:.1f}"
                    elif k=='WHEN':v=f"t={ev['time_seconds']:.2f}s"
                    elif k=='HOW':v='C <- collision(A, B)'
                    else:v='Unresolved'
                    txt(canvas,v,(sx+107,y),.46,WHITE)
            else:
                txt(canvas,'Awaiting D-C encounter',(sx+20,400),.52,MUTED)
            txt(canvas,f'TIME  {frame/FPS:5.1f}s',(35,700),.57,WHITE)
            txt(canvas,f'BALLS  {len(balls):02}',(240,700),.57,WHITE)
            txt(canvas,f'BIRTHS  {births:02}',(408,700),.57,WHITE)
            txt(canvas,f'COLLISIONS  {collision_count:03}',(580,700),.57,WHITE)
            txt(canvas,f'ENCOUNTERS  {len(question_events):02}',(847,700),.57,CYAN,2)
            for i,(name,color) in enumerate((('A: green',GREEN),('B: blue',BLUE),('Small: red',RED),
                        ('Grown: yellow',YELLOW),('D1: violet',OBS1),('D2: orange',OBS2),('D3: white',OBS3),('Event: cyan',CYAN))):
                xx=36+i*253
                cv2.circle(canvas,(xx,750),6,color,-1,cv2.LINE_AA)
                txt(canvas,name,(xx+14,756),.48,WHITE)
            if video is not None:video.write(canvas)
            if frame in capture_at:
                shot=output.with_name(f'{output.stem}_frame_{frame:04d}.png')
                cv2.imwrite(str(shot),canvas)
                captures.append(str(shot))
        if frame%FPS==0 or frame==frames-1:
            progress.append({'frame':frame,'seconds':round(frame/FPS,4),'balls':len(balls),
                'births':births,'growths':growths,'collisions':collision_count,
                'question_events':len(question_events),'c_grown':bool(c.grow) if c else False})
    if video is not None:
        video.release()
        if shutil.which('ffmpeg'):
            subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(temp),
                        '-c:v','libx264','-pix_fmt','yuv420p','-crf','24','-movflags','+faststart',str(output)],check=True)
            temp.unlink()
        else:os.replace(temp,output)
    result={
        'experiment':'QI Question Origination: projected 3D cube V5',
        'model_status':'visual analogue; question origination is not computed',
        'preceding_version':'V2 observer experiment, preserved unchanged',
        'change':'V4 cube retained; added adjustable duration and speed scaling controls',
        'seed':seed,'fps':FPS,'duration_seconds':seconds,'arena_side':ARENA,
        'dimensions':3,'max_balls':MAX_BALLS,
        'mechanics':'V4 collision/growth/spawn and read-only D interaction in 3D with adjustable speed_scale',
        'observer_rule':'D1, D2 and D3 each seek and detect original C exclusively; Qn identifies an observer-specific C access record',
        'speed_scale':speed_scale,
        'question_definition':'Encounter records document potential access, not evidence of an asked question',
        'original_colors':{'A':'green','B':'blue','C_small':'red','C_grown':'yellow','D1':'violet','D2':'orange','D3':'white','encounter_event':'cyan'},
        'first_collision':first_collision,'c_origin':c_origin,
        'birth_events':birth_events,'growth_events':growth_events,'question_events':question_events,
        'observer_colors':{'D1':'violet','D2':'orange','D3':'white'},
        'progress':progress,'final':progress[-1],
        'captures':captures,'video':str(output) if not no_video else None,
    }
    if log_path:
        target=Path(log_path);target.parent.mkdir(parents=True,exist_ok=True)
        target.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--output',default='question_origination_cube_v5.mp4')
    p.add_argument('--seconds',type=float,default=17.0)
    p.add_argument('--seed',type=int,default=14)
    p.add_argument('--event-log',default='question_origination_cube_v5_events.json')
    p.add_argument('--no-video',action='store_true')
    p.add_argument('--speed-scale',type=float,default=0.5,help='Multiply ball and observer speeds by this factor')
    p.add_argument('--captures',default='10,30,50',help='Comma-separated frame capture times (seconds)')
    args=p.parse_args()
    times=[float(v) for v in args.captures.split(',') if v.strip()] if args.captures else []
    result=generate(args.output,args.seconds,args.seed,args.event_log,args.no_video,times,args.speed_scale)
    print('Final:',result['final'])
    print('C origin:',result['c_origin'])
    print('D-observer encounter events:',[(x['question_id'],x['time_seconds'],x['c_state_at_encounter']) for x in result['question_events']])
    print('Speed scale:', args.speed_scale)
    print('Log:',args.event_log)
    if not args.no_video:print('Video:',args.output)
if __name__=='__main__':main()
