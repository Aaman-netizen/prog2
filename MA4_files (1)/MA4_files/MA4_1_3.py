
"""
Solutions to module 4
Review date:

"""

student = "Amanda Frånberg"
reviewer = ""

import math as m
import random as r
import concurrent.futures as future
from time import perf_counter as pc


def sphere_volume(n, d):
    # n is a list of set of coordinates
    # d is the number of dimensions of the sphere

    dots = [[r.uniform(-1, 1) for k in range(0, d)] for i in range(0, n)]
    squares = [(list(map(lambda x: x ** 2, dots[i][:d]))) for i in range(0, n)]
    inside = [dots[i] for i in range(0, n) if sum(squares[i]) <= 1]
    print(f'V(1)_{d} = {(len(inside) / n) * 2 ** d}')

    return (len(inside) / n) * 2 ** d


def hypersphere_exact(n, d):
    return (m.pi ** (d / 2)) / (m.gamma((d / 2) + 1))

# parallel code - parallelize for loop
def sphere_volume_parallel1(n, d, np):
     #using multiprocessor to perform 10 iterations of volume function

     dots = []
     dims = []
     for i in range(np):
         dots.append(n)
         dims.append(d)

     with future.ProcessPoolExecutor() as ex:
         vols = list(ex.map(sphere_volume, dots, dims))
     return sum(vols)/len(vols)


def sphere_volume_parallel2(n, d, np):
    # parallel code - parallelize actual computations by splitting data

    dots = []
    dims = []
    npp = n / np
    for i in range(np):
        dots.append(npp)
        dims.append(d)

    with future.ProcessPoolExecutor() as ex:
        vols = list(ex.map(sphere_volume, dots, dims))
    return sum(vols) / len(vols)

def main():
    # part 1 -- parallelization of a for loop among 10 processes
    n = 100000
    d = 11
    np = 10

    start = pc()
    for y in range(10):
        sphere_volume(n, d)
    end = pc()
    print(f'Time required for 10 loops: {round(end - start, 2)} seconds!')
    start = pc()
    sphere_volume_parallel1(n, d, np)
    end = pc()
    print(f'Time required for 10 parallell1 runs: {round(end - start, 2)} seconds!')
    start = pc()
    sphere_volume_parallel1(n, d, np)
    end = pc()
    print(f'Time required for 10 parallell2 runs: {round(end - start, 2)} seconds!')


if __name__ == '__main__':
	main()
