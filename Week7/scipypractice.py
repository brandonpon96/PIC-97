#!/usr/bin/python

import scipy.io.wavfile
from scipy import fftpack
import pylab as plt
import numpy as np

sig = scipy.io.wavfile.read('AMajor.wav')
audio = sig[1]

plt.ylabel("Amplitude")
plt.xlabel("Time")
# set the title  
plt.title("Sample Wav")
sig_fft = fftpack.fft(audio)
plt.plot(sig_fft)
plt.show()
# scipy.io.wavfile.write('A440.wav',rate,note)

# r = np.array([[np.random.rand(3)]][[np.random.rand(3)]])
# print r




# time_step = 0.02
# # period = 5.
# time_vec = np.arange(0, 20, time_step)
# # sig = np.sin(2 * np.pi / period * time_vec) + 0.5 * np.random.randn(time_vec.size)
# sample_freq = fftpack.fftfreq(sig.size, d=time_step)
# sig_fft = fftpack.fft(sig)
# plt.plot(time_vec, sig)
# plt.show()