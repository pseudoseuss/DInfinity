import numpy as np
from sympy import totient


def construct_modular_dirac(N=1000, s=1.0, P=10007):
    """
    Constructs the modular Dirac matrix D_N using a modular kernel.

    Parameters:
        N (int): Size of the operator (NxN blocks).
        s (float): Exponent applied in the denominator.
        P (int): Large prime cutoff for the cosine kernel.

    Returns:
        D_N (ndarray): The 2N x 2N modular Dirac matrix.
    """
    M = np.zeros((N, N), dtype=np.float64)
    for i in range(N):
        for j in range(N):
            phi_j = totient(j + 1)
            M[i, j] = (phi_j / (j + 1)**s) * np.cos(2 * np.pi * (i + 1) * (j + 1) / P)

    # Create block Dirac structure
    D_N = np.block([
        [np.zeros((N, N)), M],
        [M.T, np.zeros((N, N))]
    ])

    return D_N


if __name__ == "__main__":
    D = construct_modular_dirac(N=100, s=1.0)
    print("Modular Dirac matrix constructed with shape:", D.shape)
