import numpy as np

simple_arr = np.arange(15)
print(simple_arr.ndim)
print("---------------")
print(simple_arr)
print("---------------")

simple_arr = simple_arr.reshape(3, 5)  # reshape(rows, cols)
print(simple_arr)
print("---------------")
print(simple_arr.shape)
print("---------------")
print(simple_arr.ndim)
print("---------------")
print(simple_arr.size)
print("---------------")
print(simple_arr.dtype)

b = np.array([1.2, 3.5, 5.1])
print("---------------")
print(b)
print(b.dtype)

print(type(simple_arr))
