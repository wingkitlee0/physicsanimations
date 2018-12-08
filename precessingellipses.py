import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def ellipse(a, ecc, pom, theta):
    r = a*(1.0-ecc**2)/(1.0-ecc*np.cos(theta-pom))
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y

fig, ax = plt.subplots(figsize=(6,6))
ax.axis("off")
ax.set_aspect("equal")
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)
ax.scatter([0.0],[0.0],marker="*", s=200, c='C1')

tt = np.linspace(0.0, 2.0*np.pi, 200)
aa = np.array([1.0, 2.0]) # semi-major axis
er = np.array([0.1, 0.2]) # eccentricity
pr = np.array([1.0/400.0, 1.0/200.0])*2.0*np.pi # precession rate

lines = []
for i, a in enumerate(aa):
    print(a, i)
    x, y = ellipse(a, er[i], 0.0, tt)
    line, = ax.fill(x,y, fill=False, lw=2)
    lines.append(line)



def init():  # only required for blitting to give a clean slate.
    return lines


def animate(i):
    for j in range(len(lines)):
        x, y = ellipse(aa[j], er[j], pr[j]*i, tt)
        xy = np.array([ [xi,yi] for xi, yi in zip(x,y)])
        lines[j].set_xy(xy)
    return lines


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=5, blit=True, frames=400, save_count=50)

# To save the animation, use e.g.
#
# ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

#plt.show()
#ani.save("movie.mp4")
from matplotlib.animation import FFMpegWriter
writer = FFMpegWriter(fps=50, metadata=dict(artist='Kit Lee', comment="precessing ellipses"), bitrate=300)
ani.save("movie.mp4", writer=writer, dpi=150)
#ani.save("movie.mp4", writer="ffmpeg")
