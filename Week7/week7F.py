#!/usr/bin/python

import scipy.io.wavfile
from scipy import fftpack
import pylab as plt
import numpy as np

sample, audio = scipy.io.wavfile.read('wooguy.wav')
channel = audio.T[0]
sig_fft = fftpack.fft(channel)
d = len(sig_fft)/2
sig_fft[9000:9500] = 0
sig_fft[-9500:-9000] = 0
filtered = fftpack.ifft(sig_fft)
plt.plot(abs(sig_fft[:d]), 'r')
plt.show()
scipy.io.wavfile.write('nowoo.wav',sample, filtered.astype(audio.dtype))
