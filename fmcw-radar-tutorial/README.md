# FMCW Radar Tutorial

This tutorial walks from radar fundamentals to a complete FMCW radar processing pipeline.

## Learning path

1. **Radar fundamentals**: why radar exists, EM waves, and Doppler effect.
2. **CW and pulsed radar**: conceptual foundation and limits.
3. **FMCW radar**: chirp design and beat-frequency based ranging.
4. **Signal processing**: range FFT, Doppler FFT, and angle estimation.
5. **Detection**: noise/clutter handling and CFAR.
6. **Practical design**: key system parameters and trade-offs.

## Repository structure

- `01_radar_fundamentals` to `12_practical_considerations`: concept notes.
- `simulations/`: runnable Python examples.
- `interactive/radar_simulator.ipynb`: starter notebook scaffold.
- `datasets/` and `images/`: placeholders for data/figures.

## Suggested study workflow

- Read each section in order.
- Run simulation scripts after the matching theory section.
- Modify parameters (bandwidth, chirp time, noise level, number of targets) to build intuition.
