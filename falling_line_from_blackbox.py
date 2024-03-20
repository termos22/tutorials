import math
import matplotlib
from matplotlib import animation
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111)
ax.axis('off')

angle = 90
ln, = ax.plot([0], [0])

def update(frame):
    global angle

    rot = np.linspace(0, 2 * math.pi, 280)
    x = 200 * np.sin(np.linspace(0, 2 * math.pi, 280) + np.pi/2 * np.cos(angle))
    y = np.zeros(len(x))

    ln.set_xdata(x)
    ln.set_ydata(y)
    ax.set_xlim(min(x), max(x))
    ax.set_ylim(min(y), max(y))

    ax.set_theta_offset(-1 * rot[-1])
    angle += 1

    return ln, ax

ani = animation.FuncAnimation(fig, update, frames=1000, interval=100, blit=True)

plt.show()