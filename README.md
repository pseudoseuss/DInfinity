# DInfinity
Python code and numerical experiments supporting a novel spectral framework for understanding the Riemann Hypothesis using modular forms and Dirac operators.

This repository contains the numerical code and simulation tools developed for the research presented in the book:

**“Modular Resonance and the Riemann Hypothesis: A Spectral Framework for Prime Distribution and Quantum Geometry”**

We explore a new operator-theoretic model based on modular Dirac operators and resonance structures, providing both analytical constructions and numerical evidence supporting the Riemann Hypothesis through trace zeta analogs.

---

## 📁 Project Structure

- `modular_dirac.py` — Builds the modular Dirac matrix \( D_N \) from modular kernel definitions.
- `trace_zeta.py` — Computes the trace \( \mathrm{Tr}(e^{-t^2 D_K^2}) \), orbit-subtracted kernel, and defines \( \zeta_{\text{mod}}(s) \).
- `zero_comparison.py` — Compares eigenvalues to known zeta zeros and computes correlation statistics.
- `spectral_statistics.py` — Analyzes eigenvalue spacings vs GUE statistics.
- `visualize_criticalline.py` — Plots \( \zeta_{\text{mod}}(0.5 + it) \) and zero crossings.
- `demo_analysis.ipynb` — Jupyter notebook tying together all analyses and plots.

---

## 🔧 Requirements

- Python 3.10+
- NumPy
- SciPy
- Matplotlib
- mpmath
- SymPy
- (Optional) JupyterLab / Jupyter Notebook for interactive use

Install dependencies:
```bash
pip install numpy scipy matplotlib mpmath sympy
