import numpy as np

fc = 77e9
c = 3e8
lam = c / fc
d = lam / 2
Nant = 8

theta_true_deg = 20.0
theta = np.deg2rad(theta_true_deg)

n = np.arange(Nant)
phase = 2 * np.pi * d * np.sin(theta) * n / lam
x = np.exp(1j * phase)

ang_fft = np.fft.fftshift(np.fft.fft(x, 256))
spatial_freq = np.fft.fftshift(np.fft.fftfreq(256, d=1))
sin_theta = spatial_freq * lam / d
sin_theta = np.clip(sin_theta, -1, 1)
angles = np.rad2deg(np.arcsin(sin_theta))

theta_est = angles[np.argmax(np.abs(ang_fft))]
print(f'True angle: {theta_true_deg:.2f} deg')
print(f'Estimated angle: {theta_est:.2f} deg')
