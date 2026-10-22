#!/usr/bin/env python3
"""Question-origination experiment V2: one observer D, one original potential C.

New layer: violet D encounters only original C (ident=2), whether C is small/red
or grown/yellow. At each separately armed encounter, D originates a question
EVENT, logged as Q1, Q2... with WHO/WHAT/WHERE/WHEN/HOW/WHY fields.
The event leaves the physical C state unchanged and does not spawn a ball.
A lineage pointer associates each event with the archived A+B -> C birth event.

Base layer: faithfully transcribes V1's original physics, collision spawns,
color behavior and PRNG order, with its original parameters and cap. D never
participates in ordinary physics. This is an illustrative observer model; it
makes no claim to demonstrate cognitive question recognition or physical chaos.

The observer uses deterministic pursuit solely to ensure observable encounters;
this is an explicit V2 visualization choice, not a claimed theoretical rule.

Dependencies: python >=3.9, numpy, opencv-python; ffmpeg for H.264 video.
Examples:
  python question_origination_observer_v2.py --seconds 17 --output observer_v2.mp4
  python question_origination_observer_v2.py --seconds 17 --seed 14 --no-video
"""
from __future__ import annotations
import argparse
import hashlib
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
# OpenCV BGR color order. Preserve original V1 colors.
GREEN=(72,215,90)
BLUE=(250,155,55)
RED=(80,75,242)
YELLOW=(72,215,250)
VIOLET=(225,112,160)
CYAN=(255,232,38)
WHITE=(235,240,245)
MUTED=(161,174,190)
BACKGROUND=(12,15,24)
PANEL=(23,28,41)
WIDTH,HEIGHT=1420,740
LEFT=(32,159)
RIGHT=(525,159)

@dataclass
class Ball:
    ident:int
    x:float
    y:float
    vx:float
    vy:float
    r:float
    born:int
    grow:bool=False
    fixed:bool=False
    label:str=""
    prev:tuple|None=None
    def color(self):
        if self.ident==0:return GREEN
        if self.ident==1:return BLUE
        if self.grow:return YELLOW
        return RED

@dataclass
class Observer:
    x:float=337.0
    y:float=333.0
    vx:float=0.0
    vy:float=0.0
    r:float=OBSERVER_R
    active:bool=False
    contacted:bool=False
    last_event:int=-9999
    prev:tuple|None=None


def txt(img,s,pos,scale=.55,color=WHITE,thickness=1):
    cv2.putText(img,str(s),tuple(map(int,pos)),cv2.FONT_HERSHEY_SIMPLEX,scale,color,thickness,cv2.LINE_AA)

def line(img,p1,p2,color,width=1):
    cv2.line(img,tuple(map(int,p1)),tuple(map(int,p2)),color,width,cv2.LINE_AA)

def point(v):return int(round(v))

def advance_observer(d:Observer,c:Ball|None,frame:int,dt:float):
    """V2-only observer steering: D seeks C; it ignores every other ball.

    D does not force, displace, or change C. After an observation it briefly
    retreats to permit a distinct later encounter. D obeys square boundaries.
    """
    d.prev=(d.x,d.y)
    if c is None:
        # Before C exists, the observer waits at the top-right as a visible
        # spectator. No question can be originated before C's creation.
        return
    d.active=True
    dx=c.x-d.x;dy=c.y-d.y
    norm=max(math.hypot(dx,dy),.001)
    if frame-d.last_event<round(.8*FPS):
        ux,uy=-dx/norm,-dy/norm
        speed=156.0
    else:
        ux,uy=dx/norm,dy/norm
        speed=205.0
    # Smooth velocity to avoid teleportation or abrupt jitter.
    f=.22
    d.vx=(1-f)*d.vx+f*ux*speed
    d.vy=(1-f)*d.vy+f*uy*speed
    d.x+=d.vx*dt;d.y+=d.vy*dt
    if d.x<d.r:d.x=2*d.r-d.x;d.vx=abs(d.vx)
    if d.x>ARENA-d.r:d.x=2*(ARENA-d.r)-d.x;d.vx=-abs(d.vx)
    if d.y<d.r:d.y=2*d.r-d.y;d.vy=abs(d.vy)
    if d.y>ARENA-d.r:d.y=2*(ARENA-d.r)-d.y;d.vy=-abs(d.vy)


def generate(output:str='question_origination_observer_v2.mp4',seconds:float=17.0,seed:int=14,
             log_path:str|None=None, no_video:bool=False, capture_times:list[float]|None=None):
    """Return complete experiment log. Every logged collision event is deterministic.

    V1 mechanical state evolves without reference to D. V2 overlays observer
    events that originate *questions*, not new balls. Captures are optional.
    """
    rng=random.Random(seed)
    balls=[Ball(0,95,177,93,21,NORMAL_R,0,True,True,'A'),
           Ball(1,283,177,-91,21,NORMAL_R,0,True,True,'B')]
    d=Observer()
    next_id=2
    births=0;growths=0;collision_count=0
    contact_ages={}
    dark=np.array(BACKGROUND,dtype=np.float32)
    permanent=np.full((ARENA,ARENA,3),BACKGROUND,dtype=np.uint8)
    fade_secondary=permanent.copy()
    permanent_original=permanent.copy()
    first_collision=None
    c_origin=None
    events=[];birth_events=[];growth_events=[];progress=[]
    question_events=[]
    dt=1/FPS
    frames=int(round(seconds*FPS))
    video=None
    output=Path(output)
    if not no_video:
        output.parent.mkdir(parents=True,exist_ok=True)
        temp=output.with_name(output.stem+'_raw.mp4')
        video=cv2.VideoWriter(str(temp),cv2.VideoWriter_fourcc(*'mp4v'),FPS,(WIDTH,HEIGHT))
        if not video.isOpened():raise RuntimeError('Unable to open MP4 writer')
    capture_times=capture_times or []
    capture_at=set(min(frames-1,max(0,round(t*FPS))) for t in capture_times)
    captures=[]
    for frame in range(frames):
        # ORIGINAL V1 PHYSICS BEGIN. Preserve arithmetic, iteration order and
        # random consumption for frozen baseline parity.
        for b in balls:
            b.prev=(b.x,b.y,b.color())
            b.x+=b.vx*dt;b.y+=b.vy*dt
            if b.x < b.r:b.x=2*b.r-b.x;b.vx=abs(b.vx)
            if b.x > ARENA-b.r:b.x=2*(ARENA-b.r)-b.x;b.vx=-abs(b.vx)
            if b.y < b.r:b.y=2*b.r-b.y;b.vy=abs(b.vy)
            if b.y > ARENA-b.r:b.y=2*(ARENA-b.r)-b.y;b.vy=-abs(b.vy)
        spawned=[]
        for i in range(len(balls)):
            a=balls[i]
            for j in range(i+1,len(balls)):
                b=balls[j]
                dx=b.x-a.x;dy=b.y-a.y
                distance_sq=dx*dx+dy*dy
                rr=a.r+b.r
                if distance_sq >= rr*rr: continue
                dist=max(math.sqrt(distance_sq),.001)
                nx=dx/dist;ny=dy/dist
                rel=(b.vx-a.vx)*nx+(b.vy-a.vy)*ny
                overlap=rr-dist
                a.x-=nx*overlap*.51;a.y-=ny*overlap*.51
                b.x+=nx*overlap*.51;b.y+=ny*overlap*.51
                if rel < 0:
                    a.vx+=rel*nx;a.vy+=rel*ny
                    b.vx-=rel*nx;b.vy-=rel*ny
                key=(a.ident,b.ident)
                if frame-contact_ages.get(key,-999)>9 and rel < 0:
                    contact_ages[key]=frame
                    collision_count+=1
                    grown_ids=[]
                    for participant in (a,b):
                        if not participant.grow:
                            participant.r=NORMAL_R
                            participant.grow=True
                            growths+=1
                            grown_ids.append(participant.ident)
                            growth_events.append({'frame':frame,'time_seconds':round(frame/FPS,5),'ball_id':participant.ident})
                    if len(balls)+len(spawned)<MAX_BALLS:
                        mx=(a.x+b.x)/2;my=(a.y+b.y)/2
                        angle=rng.uniform(0,2*math.pi)
                        direction=(math.cos(angle),math.sin(angle))
                        sr=SMALL_R
                        proposed=None
                        for k in range(20):
                            angle+=(math.pi*(3-math.sqrt(5)))
                            ux=math.cos(angle);uy=math.sin(angle)
                            px=min(max(mx+ux*26,sr+2),ARENA-sr-2)
                            py=min(max(my+uy*26,sr+2),ARENA-sr-2)
                            if all((px-t.x)**2+(py-t.y)**2>(sr+t.r+1)**2 for t in balls+spawned):
                                proposed=(px,py,ux,uy);break
                        if proposed is not None:
                            px,py,ux,uy=proposed
                            speed=rng.uniform(90,155)
                            born=Ball(next_id,px,py,ux*speed,uy*speed,sr,frame,False,next_id==2,'C' if next_id==2 else '')
                            spawned.append(born)
                            be={'frame':frame,'time_seconds':round(frame/FPS,5),
                                'parents':[a.ident,b.ident],'child':next_id,
                                'location':{'x':round(px,5),'y':round(py,5)},
                                'collision_location':{'x':round(mx,5),'y':round(my,5)}}
                            birth_events.append(be)
                            if next_id==2:
                                c_origin=be
                            next_id+=1;births+=1
                    if first_collision is None:
                        first_collision={'frame':frame,'time_seconds':round(frame/FPS,5),'participants':[a.ident,b.ident]}
        balls.extend(spawned)
        # ORIGINAL V1 PHYSICS END.

        # V2 OBSERVER LAYER: takes a read of the existing C without altering it.
        c=balls[2] if len(balls)>2 and balls[2].ident==2 else None
        advance_observer(d,c,frame,dt)
        if c is not None:
            dist=math.hypot(d.x-c.x,d.y-c.y)
            touching=dist<=d.r+c.r
            if touching and not d.contacted and frame-d.last_event>=round(.9*FPS):
                d.last_event=frame
                qnum=len(question_events)+1
                ev={
                    'question_id':f'Q{qnum}',
                    'observer':'D',
                    'potential_id':'C',
                    'frame':frame,
                    'time_seconds':round(frame/FPS,5),
                    'c_state_at_encounter':'grown_yellow' if c.grow else 'small_red',
                    'where':{'x':round(c.x,5),'y':round(c.y,5)},
                    'interrogatives':{
                        'WHO':'observer D encountered potential C',
                        'WHAT':'C state '+('grown/yellow' if c.grow else 'small/red'),
                        'WHERE':f'C at x={c.x:.2f}, y={c.y:.2f}',
                        'WHEN':f't={frame/FPS:.3f}s, frame={frame}',
                        'HOW':'trace C (id=2) birth from original collision A+B',
                        'WHY':'unresolved; question content is not simulated',
                    },
                    'c_lineage':{
                        'original_collision':c_origin,
                        'subsequent_growth':[
                            ge for ge in growth_events if ge['ball_id']==2 and ge['frame']<=frame
                        ],
                    },
                    'event_kind':'observer_specific_question_constitution',
                }
                question_events.append(ev)
            # Arm again only after physical separation. Same contact never
            # creates repeated questions across consecutive video frames.
            d.contacted=touching

        # Two synchronized trails: one permanent, the other keeps the original
        # A/B/C lineage indefinitely while fading *only* secondary histories.
        fade_secondary=((fade_secondary.astype(np.float32)-dark)*.953+dark).astype(np.uint8)
        for b in balls:
            if b.prev is None:continue
            x0,y0,c0=b.prev
            p1=(int(x0),int(y0));p2=(int(b.x),int(b.y))
            original=b.ident<=2
            cv2.line(permanent,p1,p2,b.color(),2 if original else 1,cv2.LINE_AA)
            cv2.line(permanent_original,p1,p2,b.color(),2,cv2.LINE_AA) if original else None
            if not original:
                cv2.line(fade_secondary,p1,p2,b.color(),2,cv2.LINE_AA)
        if video is not None or frame in capture_at:
            # Composite the older original trails with newer fading secondary
            # trails without accidentally fading A, B or C themselves.
            bg=np.full_like(fade_secondary,BACKGROUND)
            bgmask=np.any(permanent_original!=bg,axis=2)
            fading=fade_secondary.copy()
            fading[bgmask]=permanent_original[bgmask]
            canvas=np.full((HEIGHT,WIDTH,3),BACKGROUND,dtype=np.uint8)
            txt(canvas,'QUESTION POTENTIAL   /   OBSERVER EXPERIMENT V2',(33,47),.78,WHITE,2)
            txt(canvas,'Frozen V1 collision system + one observer D (reads C only)',(35,73),.51,MUTED)
            for off,layer,heading in [(LEFT,permanent,'PERSISTENT HISTORY'),(RIGHT,fading,'FADING SECONDARY HISTORY')]:
                x,y=off
                txt(canvas,heading,(x,y-16),.55,WHITE)
                canvas[y:y+ARENA,x:x+ARENA]=layer
                cv2.rectangle(canvas,(x-1,y-1),(x+ARENA,y+ARENA),(96,110,134),2)
                # Transient ring, anchored to the encounter location/time.
                for ev in question_events[-4:]:
                    age=(frame-ev['frame'])/FPS
                    if 0 <= age <= 2.1:
                        pos=ev['where']; px=x+point(pos['x']);py=y+point(pos['y'])
                        rad=int(10+age*27)
                        cv2.circle(canvas,(px,py),rad,CYAN,2,cv2.LINE_AA)
                        txt(canvas,ev['question_id'],(px+12,py-14),.43,CYAN,1)
                if question_events and c_origin:
                    ev=question_events[-1]
                    age=(frame-ev['frame'])/FPS
                    if 0<=age<=3.0:
                        # Question's traced origin, from current encounter
                        # location back to C birth at the A+B collision.
                        origin=c_origin['collision_location']
                        end=ev['where']
                        p1=(x+point(origin['x']),y+point(origin['y']))
                        p2=(x+point(end['x']),y+point(end['y']))
                        # Dotted cyan linkage = information lineage, NOT a
                        # physical ball path.
                        n=max(1,int(math.dist(p1,p2)/11))
                        for i in range(0,n,2):
                            t=i/n;u=min(1,(i+1)/n)
                            pp=(int(p1[0]*(1-t)+p2[0]*t),int(p1[1]*(1-t)+p2[1]*t))
                            qq=(int(p1[0]*(1-u)+p2[0]*u),int(p1[1]*(1-u)+p2[1]*u))
                            cv2.line(canvas,pp,qq,CYAN,1,cv2.LINE_AA)
                        cv2.circle(canvas,p1,7,CYAN,1,cv2.LINE_AA)
                for b in balls:
                    cx=x+point(b.x);cy=y+point(b.y)
                    cv2.circle(canvas,(cx,cy),point(b.r+2),(23,28,37),-1,cv2.LINE_AA)
                    cv2.circle(canvas,(cx,cy),point(b.r),b.color(),-1,cv2.LINE_AA)
                    if b.ident<=2:
                        txt(canvas,b.label,(cx+12,cy-11),.43,WHITE,1)
                cv2.circle(canvas,(x+point(d.x),y+point(d.y)),point(d.r+2),(23,28,37),-1,cv2.LINE_AA)
                cv2.circle(canvas,(x+point(d.x),y+point(d.y)),point(d.r),VIOLET,-1,cv2.LINE_AA)
                txt(canvas,'D',(x+point(d.x)+12,y+point(d.y)-10),.46,WHITE,1)
            # Side ledger is informational, not a fictional generated question.
            sx=949
            cv2.rectangle(canvas,(sx,115),(1394,543),PANEL,-1)
            cv2.rectangle(canvas,(sx,115),(1394,543),(70,85,106),1)
            txt(canvas,'D  /  OBSERVER',(sx+21,145),.62,VIOLET,2)
            txt(canvas,'Only interacts with original C',(sx+21,174),.48,MUTED)
            txt(canvas,'Question events: '+str(len(question_events)),(sx+21,211),.55,WHITE)
            if c_origin:
                txt(canvas,'C originated from A+B collision',(sx+21,245),.49,YELLOW)
                txt(canvas,f"C birth  t={c_origin['time_seconds']:.2f}s",(sx+21,269),.48,MUTED)
            else:
                txt(canvas,'Awaiting first A+B collision',(sx+21,250),.50,MUTED)
            if question_events:
                ev=question_events[-1]
                txt(canvas,f"{ev['question_id']}  /  {ev['c_state_at_encounter'].replace('_',' ')}",(sx+21,312),.59,CYAN,2)
                for i,k in enumerate(('WHO','WHAT','WHERE','WHEN','HOW','WHY')):
                    y=342+i*29
                    txt(canvas,k,(sx+21,y),.44,(178,198,219),1)
                    v=ev['interrogatives'][k]
                    if k=='WHO':v='D observes C'
                    elif k=='WHAT':v=ev['c_state_at_encounter'].replace('_',' ')
                    elif k=='WHERE':v=f"x={ev['where']['x']:.1f}, y={ev['where']['y']:.1f}"
                    elif k=='WHEN':v=f"t={ev['time_seconds']:.2f}s"
                    elif k=='HOW':v='C <- collision(A, B)'
                    elif k=='WHY':v='Unresolved (no answer inferred)'
                    txt(canvas,v,(sx+101,y),.42,WHITE,1)
            else:
                txt(canvas,'Awaiting D-C encounter',(sx+21,314),.53,MUTED)
                txt(canvas,'WWWWHW appears at first contact',(sx+21,345),.44,MUTED)
            # Runtime event counts + color legend.
            txt(canvas,f'TIME  {frame/FPS:5.1f}s',(35,578),.56,WHITE)
            txt(canvas,f'BALLS  {len(balls):02}',(245,578),.56,WHITE)
            txt(canvas,f'BIRTHS  {births:02}',(427,578),.56,WHITE)
            txt(canvas,f'COLLISIONS  {collision_count:03}',(603,578),.56,WHITE)
            txt(canvas,f'QUESTIONS  {len(question_events):02}',(824,578),.56,CYAN,2)
            for i,(name,color) in enumerate([('A: green',GREEN),('B: blue',BLUE),('Small: red',RED),('Grown: yellow',YELLOW),('D: violet',VIOLET),('Q event: cyan',CYAN)]):
                xx=36+i*232
                cv2.circle(canvas,(xx,633),6,color,-1,cv2.LINE_AA)
                txt(canvas,name,(xx+14,638),.47,WHITE)
            txt(canvas,'C remains potential. Observer event creates a question record, not a new physical ball.',(36,689),.48,MUTED)
            if video is not None:video.write(canvas)
            if frame in capture_at:
                imagepath=output.with_name(f'{output.stem}_frame_{frame:04d}.png')
                cv2.imwrite(str(imagepath),canvas)
                captures.append(str(imagepath))
        if frame%FPS==0 or frame==frames-1:
            progress.append({'frame':frame,'seconds':round(frame/FPS,4),
                             'balls':len(balls),'births':births,
                             'growths':growths,'collisions':collision_count,
                             'question_events':len(question_events),
                             'c_grown':bool(c.grow) if c else False})
    if video is not None:
        video.release()
        if shutil.which('ffmpeg'):
            subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',str(temp),
                            '-c:v','libx264','-pix_fmt','yuv420p','-crf','24','-movflags','+faststart',str(output)],check=True)
            temp.unlink()
        else:os.replace(temp,output)
    result={
        'experiment':'QI Question Origination: observer layer V2',
        'model_status':'visual analog; no cognitive recognition claim',
        'frozen_base':'question_origination_sim_v1_frozen.py',
        'seed':seed,'fps':FPS,'duration_seconds':seconds,'arena_side':ARENA,
        'max_balls':MAX_BALLS,
        'mechanics':'V1 pairwise collision/growth/spawn; D does not alter V1 motion',
        'observer_rule':'D seeks and detects original C exclusively; separated encounters constitute observer-specific question events',
        'question_definition':'Event Qn marks D encounter with potential C; actual semantic content/answer not generated',
        'original_colors':{'A':'green','B':'blue','C_small':'red','C_grown':'yellow','D':'violet','question_event':'cyan'},
        'first_collision':first_collision,'c_origin':c_origin,
        'birth_events':birth_events,'growth_events':growth_events,
        'question_events':question_events,
        'progress':progress,'final':progress[-1],
        'captures':captures,
        'video':str(output) if not no_video else None,
    }
    if log_path:
        path=Path(log_path);path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    return result

def main():
    ap=argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--output',default='question_origination_observer_v2.mp4')
    ap.add_argument('--seconds',type=float,default=17.0)
    ap.add_argument('--seed',type=int,default=14)
    ap.add_argument('--event-log',default='question_origination_observer_v2_events.json')
    ap.add_argument('--no-video',action='store_true')
    ap.add_argument('--captures',default='3,8,14',help='Comma-separated frame capture times in seconds')
    args=ap.parse_args()
    cap=[float(x.strip()) for x in args.captures.split(',') if x.strip()] if args.captures else []
    result=generate(args.output,args.seconds,args.seed,args.event_log,args.no_video,cap)
    print('Final:',result['final'])
    print('C origin:',result['c_origin'])
    print('Questions:',[(e['question_id'],e['time_seconds'],e['c_state_at_encounter']) for e in result['question_events']])
    print('Event log:',args.event_log)
    if not args.no_video:print('Video:',args.output)

if __name__=='__main__':main()
