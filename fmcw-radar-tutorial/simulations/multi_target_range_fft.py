import numpy as np
import matplotlib.pyplot as plt

c = 3e8
B = 150e6
Tc = 50e-6
fs = 2e6
S = B / Tc
N = int(Tc * fs)
t = np.arange(N) / fs

ranges = np.array([15.0, 32.0, 55.0])
amps = np.array([1.0, 0.8, 0.6])

sig = np.zeros_like(t)
for a, R in zip(amps, ranges):
    fb = S * (2 * R / c)
    sig += a * np.cos(2 * np.pi * fb * t)

sig *= np.hanning(N)
fft = np.fft.rfft(sig)
freq = np.fft.rfftfreq(N, d=1 / fs)
range_axis = c * freq / (2 * S)

plt.figure(figsize=(8, 3))
plt.plot(range_axis, np.abs(fft))
plt.xlim(0, 80)
plt.title('Range FFT (Multiple Targets)')
plt.xlabel('Range (m)')
plt.ylabel('Magnitude')
plt.tight_layout()
plt.show()
