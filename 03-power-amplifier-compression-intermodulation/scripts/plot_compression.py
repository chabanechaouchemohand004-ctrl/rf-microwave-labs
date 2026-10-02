"""Plot the ZFL-2500 compression curve from the raw power-meter data.

Reads ../data/compression_powermeter_1GHz.csv, takes the small-signal gain
G0 as the median gain of the first 5 points, finds the 1 dB compression point
by linear interpolation, prints it, and writes ../img/compression_powermeter.png.

Usage: python scripts/plot_compression.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
data = np.genfromtxt(ROOT / "data" / "compression_powermeter_1GHz.csv",
                     delimiter=",", names=True)
pin, pout, gain = data["Pin_dBm"], data["Pout_dBm"], data["Gain_dB"]

g0 = float(np.median(gain[:5]))
target = g0 - 1.0
i = np.argmax(gain <= target)          # first point at or below G0 - 1 dB
t = (gain[i - 1] - target) / (gain[i - 1] - gain[i])
ip1 = pin[i - 1] + t * (pin[i] - pin[i - 1])
op1 = pout[i - 1] + t * (pout[i] - pout[i - 1])
print(f"G0 = {g0:.2f} dB, IP1dB = {ip1:.2f} dBm, OP1dB = {op1:.2f} dBm")

fig, (a, b) = plt.subplots(1, 2, figsize=(11, 4))
fig.suptitle("ZFL-2500 @ 1 GHz: power-meter measurement")
x = np.array([pin.min() - 0.5, pin.max()])
a.plot(x, x + g0, "--", color="gray", lw=1, label=f"Linear (G0 = {g0:.2f} dB)")
a.plot(pin, pout, "o-", ms=4, color="#1f4e79", label="Measured")
a.plot(ip1, op1, "o", ms=9, color="#c0392b", label=f"OP1dB = {op1:+.1f} dBm")
a.set(xlabel="Input power (dBm)", ylabel="Output power (dBm)")
a.legend(frameon=False)
b.plot(pin, gain, "o-", ms=4, color="#1f4e79")
b.axhline(g0, ls="--", color="gray", lw=1)
b.axhline(target, ls=":", color="#c0392b", lw=1)
b.plot(ip1, target, "o", ms=9, color="#c0392b")
b.annotate(f"IP1dB = {ip1:.1f} dBm", (ip1, target), (ip1 - 7, target - 2),
           arrowprops=dict(arrowstyle="-", color="#c0392b"), color="#c0392b")
b.set(xlabel="Input power (dBm)", ylabel="Gain (dB)")
for ax in (a, b):
    ax.grid(alpha=0.3)
    ax.spines[["top", "right"]].set_visible(False)
fig.tight_layout()
fig.savefig(ROOT / "img" / "compression_powermeter.png", dpi=150)
