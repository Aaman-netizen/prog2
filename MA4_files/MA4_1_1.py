
"""
Solutions to module 4
Review date:
"""

student = "Amanda Frånberg"
reviewer = ""


import random as r
import math
import matplotlib.pyplot as plt 

def approximate_pi(n): # OK (men väldigt lång)
    """Approximerar och returnerar värdet på pi genom att räkna hur många punkter som ligger innanför cirkeln."""
    x_r = []
    y_r = []
    x_b = []
    y_b = []
    for n in range(n + 1):
        x = r.uniform(-1, 1)
        y = r.uniform(-1, 1)
        if (x**2 + y**2) <= 1:
            x_r.append(x)
            y_r.append(y)
        else:
            x_b.append(x)
            y_b.append(y)

    plt.plot(x_r, y_r, 'ro', x_b, y_b, 'bo')
    plt.axis((-1, 1, -1, 1))
    plt.show()
    pi = 4*(len(x_r)/n)
    print(f'Approximation of pi: {pi}\n'
          f'Based on there being {len(x_r)} inside the circle.\n'
          f'True value of pi: {math.pi}')
    return pi
    
def main():
    dots = [1000, 10000, 100000]
    for n in dots:
        approximate_pi(n)

if __name__ == '__main__':
	main()
