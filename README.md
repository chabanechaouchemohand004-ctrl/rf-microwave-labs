# RF & Microwave Lab Portfolio

**Mohand Chabane Chaouche**, M.Sc. Communication Systems, Sorbonne Université

Looking for a 6-month **RF / microwave / SDR** internship starting February 2027 · [LinkedIn](https://www.linkedin.com/in/mohand-chabane-chaouche-9a515b2a7/)

These are three hands-on labs from the course *RF & Microwave Engineering* (UM4EE206, M1, 2025–26).
Each one covers design in a commercial EDA tool, measurement on real bench instruments, or both.

| # | Project | Tools | Key result |
|---|---------|-------|------------|
| 01 | [Low-pass filter: microstrip vs GaAs MMIC](01-lowpass-filter-microstrip-vs-mmic/) | Keysight ADS, Momentum | MMIC version is **15× shorter** and meets the 47 dB stopband spec; the microstrip version doesn't |
| 02 | [CSRR band-stop filter: 3D EM vs measurement](02-csrr-bandstop-filter-hfss-vna/) | Ansys HFSS, R&S ZNB20 VNA | Stopband measured at **2.280 GHz vs 2.272 GHz** simulated (0.35 % error) |
| 03 | [Power amplifier: compression & intermodulation](03-power-amplifier-compression-intermodulation/) | Power meter, VNA, spectrum analyzer | **OP1dB +17.3 dBm** (power meter and VNA agree within 0.5 dB), **OIP3 +28.5 dBm** (spectrum analyzer, one input level) |

<sub>The labs followed course handouts. I did all simulations, measurements and analysis on my own. Only the written lab reports were co-written in pairs (with A. Abdelmagid for labs 02 and 03), and those reports are not in this repository. The foundry layouts (UMS PH25-20) are not shown because the process design kit is licensed.</sub>
