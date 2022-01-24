
import numpy as np


n = int(input('please enter a number :'))

# 97 - 123
letters = [chr(i) for i in range(97, 123)] # a b c...

sol_dictionary = {}
# { a: a+n, b: b+n ....... }
shift = 97
for index in range(97, 123):
    sol_dictionary[chr(index)] = chr(shift + n)
    shift += 1
    if shift + n >= 123:
        shift = 97 - n


x = np.linspace(-10, 10, 80)
print(x)


print(sol_dictionary)
