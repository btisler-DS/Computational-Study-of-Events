#!/usr/bin/env python3
"""Collision-generated question-origination visual.

Run: python question_origination_sim.py --output question_origination.mp4
Dependencies: numpy, opencv-python; ffmpeg optional for H264 conversion.
Two synchronized panels: cumulative trails and fading secondary trails.
The animation is a conceptual model; it does not establish chaos or origination in AI.
"""
import argparse, math, random, subprocess, shutil, os
from dataclasses import dataclass
import cv2
import numpy as np

FPS=30
SIDE=426
ARENA=380
OX=23
OY=23
WIDTH=1040
HEIGHT=610
NORMAL_R=10.0
SMALL_R=5.5
MAX_BALLS=88
GREEN=(72,215,90)
BLUE=(250,155,55)
RED=(80,75,242)
YELLOW=(72,215,250)
WHITE=(235,240,245)
BACKGROUND=(12,15,24)

@dataclass
class Ball:
    ident: int
    x:float
    y:float
    vx:float
    vy:float
    r:float
    born:int
    grow:bool=False
    fixed:bool=False
    label:str=""
    prev:tuple=None

    def color(self):
        if self.ident == 0: return GREEN
        if self.ident == 1: return BLUE
        if self.grow: return YELLOW
        return RED


def draw_text(img,s,pos,scale=.55,color=WHITE,thickness=1):
    cv2.putText(img,s,tuple(map(int,pos)),cv2.FONT_HERSHEY_SIMPLEX,scale,color,thickness,cv2.LINE_AA)

def generate(output, seconds=45, seed=14):
    rng=random.Random(seed)
    # A and B travel toward one another so the first creation is unambiguous.
    balls=[Ball(0,95,177,93,21,NORMAL_R,0,True,True,'A'),
           Ball(1,283,177,-91,21,NORMAL_R,0,True,True,'B')]
    next_id=2
    births=0
    growths=0
    collision_count=0
    contact_ages={}
    permanent=np.zeros((ARENA,ARENA,3),np.uint8)
    fade=np.zeros_like(permanent)
    permanent[:]=BACKGROUND
    fade[:]=BACKGROUND
    last_points={}
    frames=int(seconds*FPS)
    temp=output[:-4]+'_raw.mp4' if output.endswith('.mp4') else output+'_raw.mp4'
    vw=cv2.VideoWriter(temp,cv2.VideoWriter_fourcc(*'mp4v'),FPS,(WIDTH,HEIGHT))
    if not vw.isOpened(): raise RuntimeError('Unable to create video')
    stats=[]
    dt=1/FPS
    for frame in range(frames):
        # Ball movement and wall reflection
        for b in balls:
            b.prev=(b.x,b.y,b.color())
            b.x+=b.vx*dt
            b.y+=b.vy*dt
            if b.x < b.r:
                b.x=2*b.r-b.x; b.vx=abs(b.vx)
            if b.x > ARENA-b.r:
                b.x=2*(ARENA-b.r)-b.x; b.vx=-abs(b.vx)
            if b.y < b.r:
                b.y=2*b.r-b.y; b.vy=abs(b.vy)
            if b.y > ARENA-b.r:
                b.y=2*(ARENA-b.r)-b.y; b.vy=-abs(b.vy)

        spawned=[]
        # Pairwise elastic contacts with per-pair re-arming after separation.
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
                    # Equal mass elastic collision: swap normal velocity components.
                    a.vx+=rel*nx;a.vy+=rel*ny
                    b.vx-=rel*nx;b.vy-=rel*ny
                key=(a.ident,b.ident)
                if frame-contact_ages.get(key,-999)>9 and rel < 0:
                    contact_ages[key]=frame
                    collision_count+=1
                    for participant in (a,b):
                        if not participant.grow:
                            participant.r=NORMAL_R
                            participant.grow=True
                            growths+=1
                    if len(balls)+len(spawned)<MAX_BALLS:
                        # Collision creates one new, smaller ball, with an outward trajectory.
                        mx=(a.x+b.x)/2;my=(a.y+b.y)/2
                        angle=rng.uniform(0,2*math.pi)
                        direction=(math.cos(angle),math.sin(angle))
                        sr=SMALL_R
                        # Spawn away from contact, not inside either parent.
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
                            spawned.append(Ball(next_id,px,py,ux*speed,uy*speed,sr,frame,False,next_id==2,'C' if next_id==2 else ''))
                            next_id+=1;births+=1
        balls.extend(spawned)

        # The source histories persist in both panels; derivative traces fade on right.
        fade=((fade.astype(np.float32)-np.array(BACKGROUND,dtype=np.float32))*.953+np.array(BACKGROUND,dtype=np.float32)).astype(np.uint8)
        for b in balls:
            if b.prev is None: continue
            x0,y0,c0=b.prev
            p1=(int(x0),int(y0));p2=(int(b.x),int(b.y))
            # A, B and C: trail history remains visible in both perspectives.
            original=b.ident<=2
            color=b.color()
            cv2.line(permanent,p1,p2,color,2 if original else 1,cv2.LINE_AA)
            if original:
                cv2.line(fade,p1,p2,color,2,cv2.LINE_AA)
            else:
                cv2.line(fade,p1,p2,color,2,cv2.LINE_AA)

        canvas=np.zeros((HEIGHT,WIDTH,3),np.uint8);canvas[:]=BACKGROUND
        draw_text(canvas,'QUESTION ORIGINATION  /  COLLISION-GENERATED SYSTEM',(42,40),.71,WHITE,2)
        draw_text(canvas,'ONE SIMULATION   -   TWO TRAIL PERSPECTIVES',(42,65),.43,(154,168,185))
        left=(35,113);right=(525,113)
        for off,layer,name in [(left,permanent,'PERSISTENT HISTORY'),(right,fade,'FADING SECONDARY HISTORY')]:
            x,y=off
            draw_text(canvas,name,(x,y-14),.55,WHITE,1)
            canvas[y:y+ARENA,x:x+ARENA]=layer
            cv2.rectangle(canvas,(x-1,y-1),(x+ARENA,y+ARENA),(103,116,138),2)
            for b in balls:
                cx=int(x+b.x);cy=int(y+b.y)
                cv2.circle(canvas,(cx,cy),int(round(b.r+2)),(23,28,37),-1,cv2.LINE_AA)
                cv2.circle(canvas,(cx,cy),int(round(b.r)),b.color(),-1,cv2.LINE_AA)
                if b.ident<=2:
                    draw_text(canvas,b.label,(cx+11,cy-10),.40,WHITE,1)
        draw_text(canvas,f'TIME   {frame/FPS:5.1f}s',(37,523),.55,WHITE)
        draw_text(canvas,f'BALLS   {len(balls):02}',(210,523),.55,WHITE)
        draw_text(canvas,f'GENERATIONS   {births:02}',(375,523),.55,WHITE)
        draw_text(canvas,f'COLLISIONS   {collision_count:03}',(622,523),.55,WHITE)
        # Four-state key
        legend=[('A / GREEN',GREEN),('B / BLUE',BLUE),('SMALL / RED',RED),('GROWN / YELLOW',YELLOW)]
        for i,(label,c) in enumerate(legend):
            xx=43+i*252
            cv2.circle(canvas,(xx,568),6,c,-1,cv2.LINE_AA)
            draw_text(canvas,label,(xx+13,574),.46,(201,211,222))
        vw.write(canvas)
        if frame%FPS==0:stats.append((round(frame/FPS),len(balls),births,growths))
    vw.release()
    if shutil.which('ffmpeg'):
        subprocess.run(['ffmpeg','-y','-hide_banner','-loglevel','error','-i',temp,'-c:v','libx264','-pix_fmt','yuv420p','-crf','22','-movflags','+faststart',output],check=True)
        os.remove(temp)
    else: os.replace(temp,output)
    return stats,collision_count

if __name__=='__main__':
    ap=argparse.ArgumentParser()
    ap.add_argument('--output',default='question_origination.mp4')
    ap.add_argument('--seconds',type=float,default=45)
    ap.add_argument('--seed',type=int,default=14)
    args=ap.parse_args()
    records,events=generate(args.output,args.seconds,args.seed)
    print('Final stats',records[-1], 'collisions',events)
    print('Progress samples:',records[::5])
    print('Saved:',args.output)
