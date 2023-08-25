import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig = plt.figure()
ax = plt.axes(projection='3d')

z = np.linspace(0, 1, 100)
a_initial = 25
b_initial=25
x = z * np.sin(a_initial * z)
y = z * np.cos(b_initial * z)

line, = ax.plot3D(x, y, z, 'green')

a_slider_ax = plt.axes([0.25, 0.1, 0.65, 0.03])
a_slider = Slider(a_slider_ax, 'a', 1, 50, valinit=a_initial)

b_slider_ax = fig.add_axes([0.1, 0.25, 0.0225, 0.63])
b_slider = Slider(ax=b_slider_ax, label="b",valmin=1, valmax=50, valinit=b_initial, orientation="vertical")

def update(val):
    a = a_slider.val
    b = b_slider.val
    x = z * np.sin(a * z)
    y = z * np.cos(b * z)
    line.set_data_3d(x, y, z)
    fig.canvas.draw_idle()

a_slider.on_changed(update)
b_slider.on_changed(update)

plt.show()
