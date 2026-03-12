# Chirp Signal

In an FMCW (Frequency-Modulated Continuous-Wave) radar, the transmitted waveform is a **chirp**: a sinusoid whose **instantaneous frequency** changes linearly with time.

## 1) Linear frequency sweep

For one up-chirp of duration $T_c$:

$$
f(t) = f_0 + S t, \qquad 0 \le t < T_c
$$

where:

- $f_0$ = start frequency (Hz)
- $T_c$ = chirp duration (s)
- $B$ = sweep bandwidth (Hz)
- $S$ = chirp slope (Hz/s), given by

$$
S = \frac{B}{T_c}
$$

So the end frequency of the chirp is:

$$
f_1 = f_0 + B
$$

## 2) Phase and time-domain signal

Instantaneous frequency is the derivative of phase:

$$
f(t) = \frac{1}{2\pi}\frac{d\phi(t)}{dt}
$$

Integrating for linear FMCW gives:

$$
\phi(t) = 2\pi\left(f_0 t + \frac{S}{2}t^2\right) + \phi_0
$$

A real transmitted chirp can be written as:

$$
s_{\text{tx}}(t) = A\cos\!\left(2\pi\left(f_0 t + \frac{S}{2}t^2\right)+\phi_0\right)
$$

Equivalent complex baseband form:

$$
s_{\text{tx}}(t)=A\,e^{j2\pi\left(f_0 t + \frac{S}{2}t^2\right)}
$$

## 3) Why chirps are used in FMCW radar

Because frequency changes with time, a delayed echo returns with a shifted instantaneous frequency relative to the current transmit frequency. Mixing TX and RX produces a **beat frequency** $f_b$ that is proportional to delay $\tau$:

$$
f_b = S\tau
$$

With propagation delay $\tau = \dfrac{2R}{c}$:

$$
R = \frac{c\tau}{2} = \frac{c\,f_b}{2S}
$$

where:

- $R$ = target range (m)
- $c$ = speed of light ($\approx 3\times10^8$ m/s)

## 4) Practical chirp metrics

- **Range resolution**:

$$
\Delta R = \frac{c}{2B}
$$

  Increasing bandwidth $B$ improves range resolution.

- **Maximum unambiguous range** (simplified, ADC-limited):

$$
R_{\max} \propto \frac{f_{b,\max}}{S}
$$

  Higher slope $S$ increases beat frequency for the same range, which can be good for sensitivity but may demand higher IF/ADC bandwidth.

- **Frame construction**:
  Multiple chirps are grouped into a frame. Fast-time (within chirp) estimates range, and slow-time (across chirps) estimates Doppler/velocity.

## 5) Notes on notation and preview compatibility

This page uses GitHub-friendly math delimiters:

- Inline math: `$...$`
- Block math: `$$...$$`

This should render correctly in GitHub Markdown preview.
