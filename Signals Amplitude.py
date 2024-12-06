#Author: Tarteel Alkaraan (25847208)
#Last Updated: 11th November 2024
#Reference: https://www.askpython.com/python/examples/amplitude-of-wav-files
#Import Libraries
from scipy.io import wavfile
import matplotlib.pyplot as plt
import numpy as np

#Read Sample Audio Rate And Data
rate, data = wavfile.read('ECGDataset/train/Normal/(18).wav')
print(f"number of channels = {data}")
length = data.shape[0] / rate
print(f"length = {length}s")

#Plot Audio Time And Amplitude
time = np.linspace(0., length, data.shape[0])
plt.plot(time, data, label="Audio")
plt.legend()
plt.xlabel("Time [s]")
plt.ylabel("Amplitude")
plt.show()