import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

# Physical constants
h = 6.626196e-27;   # Planck constant in erg s
c = 2.997924562e10; # Light speed in cm/s
kB = 1.380649e-16;   # Boltzmann constant erg/K

# Frequency range
nu = np.linspace(1e10, 1e15, 1000)

# Temperatures
temperatures = [3000, 4000, 5000]

# Planck spectral radiance as a function of frequency
def B_nu(nu, T):
    return (2*h*nu**3)/(c**2) / (np.exp(h*nu/(kB*T)) - 1)

# --- Custom tick formatter (a × 10^n) ---
def sci_notation(x, pos):
    if x == 0:
        return "0"
    a = f"{x:.0e}"  # like 1.23e+14
    base, exp = a.split("e")
    exp = int(exp)
    return rf"${base} \times 10^{{{exp}}}$"

# Plot
fig, ax = plt.subplots()
for T in temperatures:
    B = B_nu(nu, T)
    ax.plot(nu, B, label=f"T = {T} K")

ax.set_xlabel("Frequency (Hz)")
ax.set_ylabel(r"$B_{\nu}(T)$ (erg sr⁻¹ cm⁻² Hz⁻¹)")
ax.set_title("Blackbody Spectral Radiance vs Frequency")
ax.set_xlim(0, 1e15)
ax.legend(frameon=False)

# Apply custom notation to x-axis
ax.xaxis.set_major_formatter(FuncFormatter(sci_notation))

plt.tight_layout()
plt.show()
