"""
Solutions to module 4
Review date:
"""

student = "Amanda Frånberg"
reviewer = ""

import math as m
import random as r
import numpy as np


def sphere_volume(n, d):  # OK: list comprehension, map och lambda
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere

    dots = [[r.uniform(-1, 1) for k in range(0, d)] for i in range(0, n)]
    squares = [(list(map(lambda x: x ** 2, dots[i][:d]))) for i in range(0, n)]
    inside = [dots[i] for i in range(0, n) if sum(squares[i]) <= 1]
    print(f'V(1)_{d} = {(len(inside) / n) * 2 ** d}')

    return (len(inside) / n) * 2 ** d


def hypersphere_exact(n, d):  # OK
    return (m.pi ** (d / 2)) / (m.gamma((d / 2) + 1))


def main():
    n = 100000
    d = 11
    sphere_volume(n, d)
    print(hypersphere_exact(n, d))


if __name__ == '__main__':
    main()
