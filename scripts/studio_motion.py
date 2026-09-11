"""Color-led editorial motion assets; all drawings are original layout artwork."""
from PIL import Image, ImageDraw, ImageFont
import math

DARK='#101416'
WHITE='#F4F2EB'
BLUE='#284BE8'
CYAN='#54DCEC'
LIME='#B4E878'
CORAL='#FF866E'
MUTED='#ABB9B3'
COLORS=[CYAN,LIME,CORAL]

def ease(value):
    """Smoothstep easing for calm acceleration and a clean arrival."""
    value=max(0,min(1,value))
    return value*value*(3-2*value)

def eased_orbit(t):
    """A seamless orbit with subtle speed changes instead of mechanical rotation."""
    return t-math.sin(t*math.tau)/(math.tau*5)

def font(size,bold=False):
    return ImageFont.truetype('C:/Windows/Fonts/'+('segoeuib.ttf' if bold else 'segoeui.ttf'),size)

def text(d,xy,value,size=24,color=WHITE,bold=False):
    d.text(xy,value,font=font(size,bold),fill=color,anchor='lt')

def window(d,x,y,w,h,color,phase):
    d.rounded_rectangle((x,y,x+w,y+h),radius=8,fill=DARK,outline=color,width=3)
    d.line((x,y+26,x+w,y+26),fill=color,width=2)
    for i in range(3): d.ellipse((x+12+i*13,y+10,x+17+i*13,y+15),fill=color)
    d.rectangle((x+15,y+42,x+w*.56,y+h-17),fill=color)
    for i in range(3):
        width=(w*.25)*(0.7+0.3*math.sin(phase*2*math.pi+i))
        d.line((x+w*.65,y+46+i*20,x+w*.65+width,y+46+i*20),fill=WHITE,width=4)

def hero(w,h,t,mobile):
    im=Image.new('RGB',(w,h),BLUE); d=ImageDraw.Draw(im)
    text(d,(32,25),'MANCAR / DIGITAL PRODUCT STUDIO',16,WHITE,True)
    size=62 if mobile else 76
    for i,line in enumerate(['MADE TO','LOOK GOOD.','BUILT TO','WORK.']):
        text(d,(32,78+i*(size+3)),line,size,WHITE,True)
    cx,cy=(382,472) if mobile else (825,230)
    r=116 if mobile else 172
    d.ellipse((cx-r,cy-r,cx+r,cy+r),outline='#6E88FF',width=2)
    orbit=eased_orbit(t)
    d.arc((cx-r+13,cy-r+13,cx+r-13,cy+r-13),orbit*360,orbit*360+130,fill=CYAN,width=15)
    for i,c in enumerate([LIME,CORAL]):
        angle=2*math.pi*(orbit+i*.5)
        x=cx+math.cos(angle)*r; y=cy+math.sin(angle)*r
        d.rectangle((x-12,y-12,x+12,y+12),fill=c)
    slide=10*math.sin(t*2*math.pi)
    window(d,cx-r*.65,cy-65+slide,r*1.2,130,LIME,t)
    text(d,(32,h-42),'DESIGN  /  DEVELOPMENT  /  DIGITAL EXPERIENCES',14,WHITE)
    return im

def capabilities(w,h,t,mobile):
    im=Image.new('RGB',(w,h),DARK); d=ImageDraw.Draw(im)
    text(d,(32,26),'02 / WHAT WE BUILD',17,CYAN,True)
    text(d,(32,70),'One studio.',52 if mobile else 62,WHITE,True)
    text(d,(32,135),'Many possibilities.',45 if mobile else 62,WHITE,True)
    titles=['Web experiences','Business systems','Custom applications']
    subtitles=['Make your offer clear.','Connect the daily work.','Solve a specific problem.']
    for j in range(3):
        x=32 if mobile else 32+j*350
        y=231+j*140 if mobile else 254
        c=COLORS[j]
        d.rounded_rectangle((x,y,x+76,y+76),radius=8,fill=c)
        p=(t+j/3)%1
        movement=(1-math.cos(p*math.tau))/2
        if j==0:
            dx=4*(movement*2-1)
            d.rectangle((x+15+dx,y+20,x+61+dx,y+56),outline=DARK,width=3)
            d.line((x+15+dx,y+30,x+61+dx,y+30),fill=DARK,width=3)
        elif j==1:
            for n in range(3):
                row_phase=(p+n*.11)%1
                dy=3*((1-math.cos(row_phase*math.tau))-1)
                d.rectangle((x+17,y+15+n*17+dy,x+59,y+23+n*17+dy),fill=DARK)
        else:
            angle=eased_orbit(p)*math.tau
            for n in range(4):
                a=angle+n*math.pi/2
                px=x+38+math.cos(a)*19; py=y+38+math.sin(a)*19
                d.line((x+38,y+38,px,py),fill=DARK,width=3)
                d.ellipse((px-5,py-5,px+5,py+5),fill=DARK)
        tx=x+98 if mobile else x
        ty=y+8 if mobile else y+104
        text(d,(tx,ty),titles[j],27 if mobile else 26,c,True)
        text(d,(tx,ty+43),subtitles[j],21 if mobile else 22,MUTED)
    return im

def process(w,h,t,mobile):
    im=Image.new('RGB',(w,h),'#172D31'); d=ImageDraw.Draw(im)
    text(d,(32,26),'03 / FROM QUESTION TO PRODUCT',17,CYAN,True)
    text(d,(32,76),'Good work takes shape.',35 if mobile else 54,WHITE,True)
    labels=['Understand','Design','Build','Deliver']
    # The moving signal connects four permanent, readable steps.
    points=[(64,184+i*94) for i in range(4)] if mobile else [(72+i*300,211) for i in range(4)]
    d.line(points,fill='#46666B',width=3)
    route=min(t/.86,1)*3
    segment=min(int(route),2)
    local=route-segment if route<3 else 1
    # Pause briefly at each milestone before travelling to the next one.
    fraction=0 if local<.18 else 1 if local>.82 else ease((local-.18)/.64)
    a,b=points[segment],points[segment+1]
    reached=segment+(1 if fraction>=1 else 0)
    for j,(x,y) in enumerate(points):
        d.ellipse((x-16,y-16,x+16,y+16),fill=COLORS[j%3] if j<=reached else '#28474C')
        text(d,(x+42,y-12) if mobile else (x-36,y+39),labels[j],26 if mobile else 25,WHITE,True)
    if route<3:
        px=a[0]+(b[0]-a[0])*fraction; py=a[1]+(b[1]-a[1])*fraction
        d.ellipse((px-6,py-6,px+6,py+6),fill=WHITE)
    return im

def invitation(w,h,t,mobile):
    im=Image.new('RGB',(w,h),CORAL); d=ImageDraw.Draw(im)
    text(d,(32,26),'YOUR NEXT PROJECT / MANCAR SOFTWARE',16,DARK,True)
    lines=['STILL DOING IT','MANUALLY?']
    for i,line in enumerate(lines): text(d,(32,85+i*74),line,49 if mobile else 68,DARK,True)
    if mobile:
        x,y=410,302
    else: x,y=875,162
    # Ease the arrow at each end of its short diagonal travel.
    travel=(1-math.cos(t*math.tau))/2
    shift=14*(travel*2-1)
    # A large diagonal arrow glides through concentric corner frames.
    for i in range(3):
        q=25+i*22
        d.line((x-q,y+q,x-q,y-q,x+q,y-q),fill='#B14F43',width=2)
    d.line((x-42+shift,y+42-shift,x+35+shift,y-35-shift),fill=DARK,width=10)
    d.line((x-9+shift,y-35-shift,x+35+shift,y-35-shift,x+35+shift,y+9-shift),fill=DARK,width=10)
    text(d,(32,h-44),'SHOW US ONE TASK YOU WANT TO IMPROVE',17 if mobile else 22,DARK,True)
    return im

def save(frames,stem):
    # Sample all motion states into one palette so text and colors never shimmer.
    samples=Image.new('RGB',(256*8,128))
    for j in range(8):
        sample=frames[j*len(frames)//8].resize((256,128))
        samples.paste(sample,(256*j,0))
    palette=samples.quantize(colors=128)
    frames[0].save(str(stem)+'.png')
    indexed=[frame.quantize(palette=palette,dither=Image.Dither.NONE) for frame in frames]
    indexed[0].save(str(stem)+'.gif',save_all=True,append_images=indexed[1:],duration=110,loop=0,optimize=True,disposal=1)

def build_studio(out):
    layouts=[('mancar-studio-cover',hero,450,670),('mancar-capabilities',capabilities,470,680),('mancar-approach',process,340,530),('mancar-contact',invitation,320,410)]
    for mobile in (False,True):
        for name,render,desktop_h,mobile_h in layouts:
            w=560 if mobile else 1080; h=mobile_h if mobile else desktop_h
            frames=[render(w,h,i/72,mobile) for i in range(72)]
            if render is process:
                # Resolve the linear story back to its first state without a hard loop cut.
                last_state=frames[-8]
                for i in range(1,8):
                    frames[-8+i]=Image.blend(last_state,frames[0],ease(i/8))
            save(frames,out/(name+('-mobile' if mobile else '')))
