import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider

# Generate initial data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Set up figure and axis
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)  # Make room for slider

# Plot initial data
line, = ax.plot(x, y)

# Set up slider
axcolor = 'lightgoldenrodyellow'
ax_slider = plt.axes([0.2, 0.1, 0.6, 0.03], facecolor=axcolor)
slider_range = Slider(ax_slider, 'X Range', 0.1, 10.0, valinit=2.0)


# Update function for slider
def update(val):
    # Get slider value and update x range and label
    x_range = slider_range.val
    x_new = np.linspace(0, x_range * np.pi, 100)
    ax.set_xlim([x_new[0], x_new[-1]])  # update x-axis limits
    ax.set_xlabel(f'x range: {x_new[0]:.2f} - {x_new[-1]:.2f}')  # update x-axis label

    # Update data and redraw plot
    line.set_xdata(x_new)
    line.set_ydata(np.sin(x_new))
    fig.canvas.draw_idle()


# Set slider update function
slider_range.on_changed(update)

# Show plot
plt.show()