#wykres ma płynąć
#taki jakby gif
#np usuwamy najstarszą i dodajemy nową i wtedy jest płynne
#lista na 26.04
#jak będzie widać skoki to 4 jak płynnie to 5

import matplotlib.pyplot as plt
import numpy as np
import time
import neurokit2 as nk

fig = plt.figure()
ax = fig.add_subplot(111)


# eog_signal = nk.data("eog_100hz")
#
# # Process it
# # some X and Y data
# signals, info = nk.eog_process(eog_signal, sampling_rate=100)

ecg = nk.ecg_simulate(duration=15, sampling_rate=250, heart_rate=70)

# Process it
signals, info = nk.ecg_process(ecg, sampling_rate=250)
# data = signals['EOG_Raw']
data = signals['ECG_Raw']
size = len(data)
x = np.arange(size)
y = data
window_size = 250
li, = ax.plot(x[0:window_size], y[0:window_size])
ax.set_ylim([np.min(y), np.max(y)])

# draw and show it
ax.relim()
ax.autoscale_view(True,True,True)
fig.canvas.draw()


i = 0
# loop to update the data
while i < size:
    try:
        y_new = y[0+i:window_size+i]
        x_new = x[0+i:window_size+i]
        i += 5
        # set the new data
        x_new = np.linspace(0+i, window_size+i, window_size)
        ax.set_xlim([x_new[0], x_new[-1]])  # update x-axis limits

        li.set_ydata(y_new)
        li.set_xdata(x_new)
        fig.canvas.draw()

        # update the plot and pause
        plt.pause(0.1)
    except KeyboardInterrupt:
        break

plt.show()
