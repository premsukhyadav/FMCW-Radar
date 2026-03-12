import numpy as np
import matplotlib.pyplot as plt

fc = 77e9
B = 200e6
Tc = 40e-6
fs = 5e6

N = int(Tc * fs)
t = np.arange(N) / fs
S = B / Tc
phase = 2 * np.pi * (fc * t + 0.5 * S * t**2)
chirp = np.cos(phase)

plt.figure(figsize=(8, 3))
plt.plot(t * 1e6, chirp)
plt.title('FMCW Chirp (Time Domain)')
plt.xlabel('Time (us)')
plt.ylabel('Amplitude')
plt.tight_layout()
plt.show()
