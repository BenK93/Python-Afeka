#! /usr/bin/env phyton 3

import numpy as np
from matplotlib import pyplot as plt

# Q1 - secret code letters dictionary
n = int(input('please enter a number :'))
chr_nums = list(range(97, 123))
chrs = [chr(i) for i in chr_nums]
d = {v: chrs[(i+n) % len(chrs)] for i, v in enumerate(chrs)}
print(d)

# Q2 - create a 2D matrix, f
x = np.linspace(-10, 10, 80)
y = np.linspace(-10, 10, 80)
a = 1
b = -1
f = np.zeros([x.shape[0], y.shape[0]])
for i, x1 in enumerate(x):
    for j, y1 in enumerate(y):
        f[i, j] = a*x1 + b*y1 + (a**2)*(b**2)*x1*y1

plt.figure("func3D")
print(x.shape, y.shape, f.shape)
plt.contourf(x, y, f)
plt.savefig("func3D.png")
plt.show()

# Q3 create frev, a mirror image of f matrix in x dimension
# concatenate f and frev in the column axis
# to give f_adj, a 80X160 array
f_rev = f[:, ::-1]
f_adj = np.column_stack([f, f_rev])

plt.figure("f_adj")
plt.contourf(np.linspace(-20, 20, 160), y, f_adj)
plt.savefig("f_adj.png")
plt.show()

# Q4 add a mirror image of f_adj in the rows dimension to f_adj itself
# i.e., the dimension of the new matrix should be 160X160
# hint: use np.append in the right axis
f_extended = np.append(f_adj, f_adj[::-1], axis=0)

plt.figure("f_extended")
plt.contourf(np.linspace(-20, 20, 160), np.linspace(-20, 20, 160), f_extended)
plt.savefig("f_extended.png")
plt.show()

# Q5 slice out the core of f_extended matrix,
# to include only 80X80 array points with full symmetry
# in both the row and column dimensions
# hint: see figure to advice for the slicing boundaries
f_symmetric = f_extended[40:120, 40:120]
plt.figure("f_symmetric")
plt.contourf(x, y, f_symmetric)
plt.savefig("f_symmetric.png")
plt.show()

# Q6 test "f_symmetric"'s symmetry:
# test if all points in the upper and in the lower half
# of the array in the row's dimension are identical.
# hint: you should compare all values from the beginning of a row
# to the middle of the row, with all values from the end of the row
# to the middle of it for every column,
# and then test if equality holds in all columns

symmetry = np.array([])
for j in range(f_symmetric.shape[1]):
    up = f_symmetric[:int(f_symmetric.shape[0]/2), j]
    down = f_symmetric[int(f_symmetric.shape[0]/2):f_symmetric.shape[0], j]
    temp = np.all(up == down[::-1])
    symmetry = np.append(symmetry, temp)
if np.all(symmetry):
    print(symmetry)
    print("f_symmetric is fully symmetric in the column axis")
