
import numpy as np
from matplotlib import pyplot as plt

# n = int(input('please enter a number :'))

# 97 - 123
letters = [chr(i) for i in range(97, 123)] # a b c...

# sol_dictionary = {}
# # { a: a+n, b: b+n ....... }
# shift = 97
# for index in range(97, 123):
#     sol_dictionary[chr(index)] = chr(shift + n)
#     shift += 1
#     if shift + n >= 123:
#         shift = 97 - n


x = np.linspace(-10, 10, 80)
y = np.linspace(-10, 10, 80)
a = 1
b = -1
f = np.zeros([x.shape[0], y.shape[0]])
i = 0
for x_num in x:
    j = 0
    for y_num in y:
        f[i, j] = a * x_num + b * y_num + (a**2)*(b**2)*x_num*y_num
        j += 1
    i += 1

plt.contourf(x, y, f)
plt.savefig("func3D.png")
plt.show()

# f_adj = f + f[:, ::-1]
f_adj = np.concatenate([f, f[:, ::-1]], axis=1)
new_x = np.linspace(-20,20, 160)
print(f_adj.shape)

plt.contourf(new_x, y, f_adj)
plt.savefig("f_adj.png")
plt.show()