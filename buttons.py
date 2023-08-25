import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import matplotlib.widgets as widgets
import neurokit2 as nk
import numpy as np

fig, ax = plt.subplots(figsize=(10, 6))
fig.subplots_adjust(right=0.8)

ecg = nk.ecg_simulate(duration=150, sampling_rate=250, heart_rate=70)
signals, info = nk.ecg_process(ecg, sampling_rate=250)
data = signals['ECG_Raw']
size = len(data)
x = np.arange(size)
y = data
window_size = 250
li, = ax.plot(x[0:window_size], y[0:window_size])
ax.set_ylim([np.min(y), np.max(y)])



# these are matplotlib.patch.Patch properties
props = dict(boxstyle='round', facecolor='grey', alpha=0.5)

# textstr = '\n'.join([
#     r'$\mu=%.2f$' % (np.mean(ts)),
#     r'$\sigma=%.2f$' % (np.std(ts)),
#     r'$max=%.2f$' % (np.max(ts)),
#     r'$min=%.2f$' % (np.min(ts)),
#     r'$median=%.2f$' % (np.median(ts)),
#     r'$Kurt=%.2f$' % (kurtosis(ts)),
#     r'$Entropy=%.2f$' % (nolds.sampen(ts)),
#     r'$Corr Dim=%.2f$' % (nolds.corr_dim(ts, 1)),
#     r'$Hurst=%.2f$' % (nolds.hurst_rs(ts)),
# ])
# place a text box in upper left in axes coords



i = 0
moving = False

def calculate_heartbeats():


    heartbeats = []
    for i, value in enumerate(y):
        if value >= 0.9:  # Assuming a threshold of 1 to identify heartbeats
            heartbeats.append(i)

    selected_indices = []
    current_group = [heartbeats[0]]
    for i in range(1, len(heartbeats)):
        if heartbeats[i] - heartbeats[i-1] == 1:
            current_group.append(heartbeats[i])
        else:
            selected_indices.append(max(current_group, key=lambda x: y[x]))
            current_group = [heartbeats[i]]

    # Add the last group of indices
    selected_indices.append(max(current_group, key=lambda x: y[x]))

    lengths = []
    for i in range(len(selected_indices) - 1):
        length = selected_indices[i+1] - selected_indices[i]
        lengths.append(length)

    return lengths


lengths = calculate_heartbeats()


j = round(i/200)
if j + 50*200 < len(x):
    max_l = np.max(lengths[j:j + 50])
    min_l = np.min(lengths[j:j + 50])
else:
    max_l = np.max(lengths[j:])
    min_l = np.min(lengths[j:])

difference = max_l - min_l
textstr = f"Max: {max_l}\nMin: {min_l}\nDifference: {difference}"

box = plt.text(1.05, 0.65, textstr, transform=ax.transAxes, fontsize=14,
               verticalalignment='top', bbox=props)

def update_box():
    global box, i
    box.remove()
    j = round(i/200)
    next = 10
    if j + next < len(lengths):
        max_l = np.max(lengths[j:j + next])
        min_l = np.min(lengths[j:j + next])
    elif j<len(lengths):
        max_l =210
        min_l=200
    else:
        max_l = np.max(lengths[j:])
        min_l = np.min(lengths[j:])

    difference = max_l - min_l
    textstr = f"Max: {max_l}\nMin: {min_l}\nDifference: {difference}"

    box = plt.text(1.05, 0.65, textstr, transform=ax.transAxes, fontsize=14,
                   verticalalignment='top', bbox=props)


def start(event):
    global moving
    moving = True
    run_while_loop()


def stop(event):
    global moving
    moving = False


def right(event):
    global moving, i
    if moving:
        return

    i += 20
    if window_size + i > len(x):
        i = len(x) - window_size - 1

    y_new = y[0 + i:window_size + i]
    x_new = x[0 + i:window_size + i]
    i += 5
    x_new = np.linspace(0 + i, window_size + i, window_size)
    ax.set_xlim([x_new[0], x_new[-1]])
    li.set_ydata(y_new)
    li.set_xdata(x_new)

    update_box()

    fig.canvas.draw()


def left(event):
    global moving, i
    if moving:
        return

    i -= 20
    if i < 0:
        i = 0

    y_new = y[0 + i:window_size + i]
    x_new = x[0 + i:window_size + i]
    i += 5
    x_new = np.linspace(0 + i, window_size + i, window_size)
    ax.set_xlim([x_new[0], x_new[-1]])
    li.set_ydata(y_new)
    li.set_xdata(x_new)

    update_box()

    fig.canvas.draw()


def screen_shot(event):
    start_button.ax.set_visible(False)
    stop_button.ax.set_visible(False)
    right_button.ax.set_visible(False)
    left_button.ax.set_visible(False)
    screen_shot_button.ax.set_visible(False)

    fig.savefig('screenshot.png')

    start_button.ax.set_visible(True)
    stop_button.ax.set_visible(True)
    right_button.ax.set_visible(True)
    left_button.ax.set_visible(True)
    screen_shot_button.ax.set_visible(True)
    # Open new figure and axes
    fig2, ax2 = plt.subplots()

    # Load and display the saved image
    img = mpimg.imread('screenshot.png')
    ax2.imshow(img)
    ax2.axis('off')

    # Show the new plot
    plt.show()


def run_while_loop():
    global moving, i
    while moving:

        i += 5
        if window_size + i > len(x):
            i = 0

        y_new = y[0 + i:window_size + i]
        x_new = x[0 + i:window_size + i]


        x_new = np.linspace(0 + i, window_size + i, window_size)
        ax.set_xlim([x_new[0], x_new[-1]])
        li.set_ydata(y_new)
        li.set_xdata(x_new)

        update_box()


        fig.canvas.draw()
        plt.pause(0.1)


# create buttons
start_ax = plt.axes([0.2, 0.9, 0.1, 0.075])
start_button = widgets.Button(start_ax, 'Start')
start_button.on_clicked(start)

stop_ax = plt.axes([0.32, 0.9, 0.1, 0.075])
stop_button = widgets.Button(stop_ax, 'Stop')
stop_button.on_clicked(stop)

right_ax = plt.axes([0.56, 0.9, 0.1, 0.075])
right_button = widgets.Button(right_ax, 'Right')
right_button.on_clicked(right)

left_ax = plt.axes([0.44, 0.9, 0.1, 0.075])
left_button = widgets.Button(left_ax, 'Left')
left_button.on_clicked(left)

screen_shot_ax = plt.axes([0.68, 0.9, 0.15, 0.075])
screen_shot_button = widgets.Button(screen_shot_ax, 'Screenshot')
screen_shot_button.on_clicked(screen_shot)

plt.show()
