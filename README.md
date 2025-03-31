# Modular Resonance and the Riemann Hypothesis

This repository contains the source code and numerical tools used to support the operator-theoretic framework for the Riemann Hypothesis, based on modular resonance and spectral zeta methods.

The work is described in the book:  
**"Modular Resonance, Dirac Operators, and the Riemann Hypothesis"**

> ⚠️ This repository is a work-in-progress companion to the manuscript.  
> All results are reproducible with the included scripts and notebook.

---

## 📦 Contents

- `modular_dirac.py` — Generates the modular Dirac matrix \( D_N \)
- `trace_zeta.py` — Computes \( \zeta_{\mathrm{mod}}(s) \) via trace integrals
- `zero_comparison.py` — Compares eigenvalues to Riemann zeta zeros
- `spectral_statistics.py` — Plots spacing distribution and GUE comparison
- `visualize_criticalline.py` — Evaluates \( \zeta_{\mathrm{mod}}(0.5 + it) \)
- `demo_analysis.ipynb` — Full interactive walkthrough of all steps

---

## 🛠 Requirements

Tested on **Python 3.10+** with the following libraries:

```bash
pip install numpy scipy matplotlib mpmath sympy

Run scripts individually:
python modular_dirac.py
python trace_zeta.py
python zero_comparison.py
python spectral_statistics.py
python visualize_criticalline.py

For a full explanation of the theory, simulation design, and analytic framework, refer to the book and Appendix.
