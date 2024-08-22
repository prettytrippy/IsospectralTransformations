from sympy import symbols, Matrix, simplify
import numpy as np
from random import *

def make_symbolic_identity(n):
    I = np.zeros((n, n))
    for i in range(n):
        I[i][i] = symbols('x')
    return Matrix(I)

def isospectral_transform(M, s):
    rows, cols = M.shape
    if rows != cols or s >= rows: 
        print("Go fuck yourself")
        return None
    A = M[0:s, 0:s]
    B = M[0:s, s:]
    C = M[s:, 0:s]
    D = M[s:, s:]
    I = make_symbolic_identity(D.shape[0])
    return (A - B * ((D - I).inv()) * C).applyfunc(simplify)

if __name__ == "__main__":
    n = 8
    s = 4
    twod_array = np.random.randn(n, n)

    M = Matrix(twod_array)
    Mp = isospectral_transform(M, n-s)
