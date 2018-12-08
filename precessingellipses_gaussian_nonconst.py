import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

ARTIST="Kit Lee"
COMMENT="precessing ellipses. precession is not constant."
OUTPUTFILE="gaussian_nonconst.mp4"

def ellipse(a, ecc, pom, theta):
    r = a*(1.0-ecc**2)/(1.0-ecc*np.cos(theta-pom))
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y

rmin = 1.0
rmax = 10.0

fig, ax = plt.subplots(figsize=(6,6))
ax.axis("off")
ax.set_aspect("equal")
ax.set_xlim(-rmax*1.5,rmax*1.5)
ax.set_ylim(-rmax*1.5,rmax*1.5)
ax.scatter([0.0],[0.0],marker="*", s=200, c='C1')

nrings = 20

rmid = 0.5*(rmax+rmin)
tt = np.linspace(0.0, 2.0*np.pi, 200)
xx = np.linspace(0.0, 1.0, nrings)
aa = xx*(rmax-rmin)+rmin # semi-major axis
er = 0.1*np.exp(-( (aa-rmid)/2.0)**2)+0.1 # eccentricity
pr = 0.005*xx*2.0*np.pi # precession rate

lines = []
for i, a in enumerate(aa):
    print(a, i)
    x, y = ellipse(a, er[i], 0.0, tt)
    line, = ax.fill(x,y, fill=False, lw=2, alpha=0.5)
    lines.append(line)



def init():  # only required for blitting to give a clean slate.
    for j in range(len(lines)):
        x, y = ellipse(aa[j], er[j], 0.0, tt)
        xy = np.array([ [xi,yi] for xi, yi in zip(x,y)])
        lines[j].set_xy(xy)
    return lines

def init():  # only required for blitting to give a clean slate.
    for j in range(len(lines)):
        x, y = ellipse(aa[j], er[j], 0.0, tt)
        xy = np.array([ [xi,yi] for xi, yi in zip(x,y)])
        lines[j].set_xy(xy)
    return lines


def animate(i):
    for j in range(len(lines)):
        x, y = ellipse(aa[j], er[j], pr[j]*i, tt)
        xy = np.array([ [xi,yi] for xi, yi in zip(x,y)])
        lines[j].set_xy(xy)
    return lines


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=1, blit=True, frames=800, save_count=50)

from matplotlib.animation import FFMpegWriter
writer = FFMpegWriter(fps=50, metadata=dict(artist=ARTIST, comment=COMMENT), bitrate=300)
ani.save(OUTPUTFILE, writer=writer)