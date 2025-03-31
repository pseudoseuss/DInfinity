import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import gaussian_kde

# --- Load eigenvalues (compressed modular Dirac spectrum) ---
# Replace with actual loading method or simulated data
lambda_n = np.loadtxt("compressed_eigenvalues.txt")

# --- Compute Nearest-Neighbor Spacing ---
lambda_n_sorted = np.sort(lambda_n)
spacings = np.diff(lambda_n_sorted)

# --- Normalize Spacings ---
mean_spacing = np.mean(spacings)
norm_spacings = spacings / mean_spacing

# --- GUE Distribution Function ---
def gue_pdf(s):
    return (np.pi / 2) * s * np.exp(- (np.pi / 4) * s**2)

# --- Plot Histogram vs. GUE ---
s_vals = np.linspace(0, 4, 400)
kde = gaussian_kde(norm_spacings)

plt.figure(figsize=(8,5))
plt.hist(norm_spacings, bins=50, density=True, alpha=0.5, label="Empirical spacing")
plt.plot(s_vals, gue_pdf(s_vals), 'r--', label="GUE prediction")
plt.plot(s_vals, kde(s_vals), 'b-', label="KDE")
plt.title("Nearest-Neighbor Spacing Distribution")
plt.xlabel("Normalized spacing")
plt.ylabel("Probability density")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig("spacing_vs_gue.png")
plt.show()
