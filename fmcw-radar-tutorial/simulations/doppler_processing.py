import numpy as np

fc = 77e9
c = 3e8
lam = c / fc
Tr = 60e-6
M = 128
v_true = 6.5

fD = 2 * v_true / lam
m = np.arange(M)
slow_time_signal = np.exp(1j * 2 * np.pi * fD * m * Tr)

spec = np.fft.fftshift(np.fft.fft(slow_time_signal * np.hanning(M)))
freq = np.fft.fftshift(np.fft.fftfreq(M, d=Tr))
vel_axis = freq * lam / 2
v_est = vel_axis[np.argmax(np.abs(spec))]

print(f'True velocity: {v_true:.2f} m/s')
print(f'Estimated velocity: {v_est:.2f} m/s')
