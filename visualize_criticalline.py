import numpy as np
import matplotlib.pyplot as plt
from scipy.special import gamma
from scipy.integrate import quad
from trace_zeta import modular_trace

# Define zeta_mod(0.5 + it)
def zeta_mod_critical_line(t, alpha=0.0005):
    def integrand(u):
        trace_val = modular_trace(u)
        return u**(-0.5) * trace_val * np.cos(t * np.log(u))

    integral, _ = quad(integrand, 1e-6, 20, limit=100)
    return alpha / gamma(0.5) * integral

# Evaluate zeta_mod on the critical line
t_vals = np.linspace(0.1, 50, 500)
zeta_vals = np.array([zeta_mod_critical_line(t) for t in t_vals])

# Plot real part and mark zero crossings
plt.figure(figsize=(10, 6))
plt.plot(t_vals, zeta_vals.real, label='Re($\zeta_{mod}(0.5 + it)$)')
plt.axhline(0, color='black', linestyle='--')
plt.xlabel('t')
plt.ylabel('Re($\zeta_{mod}$)')
plt.title('Visualization of $\zeta_{mod}(0.5 + it)$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
