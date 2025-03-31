"""
trace_zeta.py

Computes the trace of the heat kernel Tr(exp(-t^2 D_K^2)) for a modular Dirac operator D_K,
performs orbit subtraction to remove low-frequency artifacts, and defines the modular
zeta function \zeta_mod(s) using numerical integration.

Functions:
- compute_trace(D, t): Returns trace of heat kernel at time t.
- trace_subtracted(D, t, orbits): Subtracts modeled orbit terms.
- zeta_mod(D, s, orbits, alpha): Computes modular zeta function via quadrature.

Dependencies:
- numpy
- scipy (integrate, special)
"""

import numpy as np
from scipy import integrate, special

def compute_trace(D, t):
    eigvals = np.linalg.eigvalsh(D)
    return np.sum(np.exp(-t**2 * eigvals**2))

def trace_subtracted(D, t, orbits):
    trace_val = compute_trace(D, t)
    orbit_sum = sum(np.exp(-t * f**2) for f in orbits)
    return trace_val - orbit_sum

def zeta_mod(D, s, orbits=None, alpha=0.0005):
    if orbits is None:
        orbits = list(range(2, 40, 2))

    def integrand(t):
        if t == 0:
            return 0
        return t**(s - 1) * trace_subtracted(D, t, orbits)

    integral, _ = integrate.quad(integrand, 0, np.inf, limit=100, epsabs=1e-10)
    return alpha * integral / special.gamma(s)

if __name__ == "__main__":
    from modular_dirac import build_modular_dirac
    D = build_modular_dirac(N=500)
    s = 2.0
    zeta_val = zeta_mod(D, s)
    print(f"zeta_mod({s}) = {zeta_val:.10f}")
