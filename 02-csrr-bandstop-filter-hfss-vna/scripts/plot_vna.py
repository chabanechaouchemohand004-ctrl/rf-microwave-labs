"""Plot the measured S11 and S21 of the CSRR board from the VNA .s2p file.

Reads ../data/csrr_vna_measurement.s2p (R&S ZNB20, 1-3 GHz, 1601 points,
magnitude/angle format), prints the S21 notch and S11 null, and writes
../img/vna_measured_vs_hfss.png. The two HFSS markers are the values read
from my HFSS sweep (S11 null and S21 notch), not a full simulated curve.

Usage: python scripts/plot_vna.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
rows = [l.split() for l in open(ROOT / "data" / "csrr_vna_measurement.s2p")
        if l.strip() and l[0] not in "!#"]
a = np.array(rows, float)
f = a[:, 0] / 1e9
db = lambda mag: 20 * np.log10(mag)
s11, s21, s12 = db(a[:, 1]), db(a[:, 3]), db(a[:, 5])

i21 = np.argmin(s21)
i11 = np.argmin(s11)
print(f"S21 notch: {f[i21]:.3f} GHz, {s21[i21]:.1f} dB (S11 there: {s11[i21]:.1f} dB)")
print(f"S11 null:  {f[i11]:.3f} GHz, {s11[i11]:.1f} dB (S21 there: {s21[i11]:.2f} dB)")

HFSS_NOTCH = (2.272, -24.5)   # S21 notch, HFSS
HFSS_NULL = (1.746, -37.2)    # S11 null, HFSS

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.plot(f, s21, color="#1f4e79", lw=1.6, label="S21 measured")
ax.plot(f, s11, color="#d97706", lw=1.6, label="S11 measured")
ax.plot(*HFSS_NOTCH, "o", mfc="none", mec="#1f4e79", ms=9, mew=2, label="S21 notch, HFSS")
ax.plot(*HFSS_NULL, "o", mfc="none", mec="#d97706", ms=9, mew=2, label="S11 null, HFSS")
ax.annotate(f"{f[i21]:.3f} GHz\n{s21[i21]:.1f} dB", (f[i21], s21[i21]),
            (f[i21] + 0.12, s21[i21] + 3), fontsize=9)
ax.set(xlabel="Frequency (GHz)", ylabel="Magnitude (dB)", xlim=(1, 3), ylim=(-60, 3),
       title="CSRR band-stop filter: VNA measurement vs HFSS markers")
ax.grid(alpha=0.3)
ax.spines[["top", "right"]].set_visible(False)
ax.legend(frameon=False, loc="lower right", fontsize=9)
fig.tight_layout()
fig.savefig(ROOT / "img" / "vna_measured_vs_hfss.png", dpi=150)
