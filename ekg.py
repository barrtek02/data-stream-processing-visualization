# pypi org project neurokit2
# Load NeuroKit and other useful packages


# https://pypi.org/project/neurokit2/

# phisionet
# Download example data
# EKG w milivoltach/innych jednostkach
# sygnały piknięcia serca na sekunde
# kilka wykresów na różne sposoby przedstawienia, przykład 3d




import pandas as pd
import neurokit2 as nk
from matplotlib import pyplot as plt

# Generate 15 seconds of ECG signal (recorded at 250 samples / second)
ecg = nk.ecg_simulate(duration=15, sampling_rate=250, heart_rate=70)

# Process it
signals, info = nk.ecg_process(ecg, sampling_rate=250)

# Visualise the processing
nk.ecg_plot(signals, sampling_rate=250)
plt.show()


# Import EOG data
eog_signal = nk.data("eog_100hz")

# Process it
signals, info = nk.eog_process(eog_signal, sampling_rate=100)

# Plot
nk.eog_plot(signals, info, sampling_rate=100)
plt.show()