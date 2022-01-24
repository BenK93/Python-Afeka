import math


def calc_sin(radians, prescision_level):
    accurate_val = math.sin(radians)
    returned_val = radians
    error = abs(accurate_val - returned_val)
    factorial_start = 3
    while error >= prescision_level:
        print(error, factorial_start, returned_val)
        fac = factorial(factorial_start)
        returned_val -= (returned_val**factorial_start) / fac
        factorial_start += 2
        error = accurate_val - returned_val
    return returned_val


def factorial(num):
    if num == 1:
        return num
    return num * factorial(num-1)


print(factorial(5))

print("Sins 90 degrees = ", math.sin(math.pi / 2))
print("Sins 90 degrees = ", calc_sin(math.pi / 2, 0.01))
print("PI = ", math.pi)
