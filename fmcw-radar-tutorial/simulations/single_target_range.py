import numpy as np

c = 3e8
B = 200e6
Tc = 40e-6
S = B / Tc
R_true = 25.0

# Beat frequency for one target
fb = S * (2 * R_true / c)
R_est = c * fb / (2 * S)

print(f'True range: {R_true:.2f} m')
print(f'Beat frequency: {fb/1e3:.2f} kHz')
print(f'Estimated range: {R_est:.2f} m')
