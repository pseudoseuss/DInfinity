# zero_comparison.py

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

# Load eigenvalues from modular Dirac operator (compressed)
eigenvalues = np.loadtxt("eigenvalues_tanh.txt")  # Assumes tanh-compressed

# Load known nontrivial zeros of zeta (imaginary parts)
zeta_zeros = np.loadtxt("zeta_zeros.txt")

# Normalize sequences to the same scale
eigenvalues_rescaled = np.interp(np.arange(len(zeta_zeros)), np.arange(len(eigenvalues)), eigenvalues)

# Compute correlation
corr, _ = pearsonr(eigenvalues_rescaled, zeta_zeros)
print(f"Correlation with Riemann zeros: {corr:.4f}")

# Plot comparison
plt.figure(figsize=(10, 5))
plt.plot(eigenvalues_rescaled, label="Rescaled Eigenvalues", lw=2)
plt.plot(zeta_zeros, label="Riemann Zeta Zeros", lw=2, linestyle='--')
plt.title("Comparison of Compressed Modular Spectrum vs Zeta Zeros")
plt.xlabel("Index")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("comparison_plot.png")
plt.show()
