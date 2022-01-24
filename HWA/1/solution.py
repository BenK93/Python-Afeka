number = 88240


def easy_transform(num):
    return bin(num)


def transform(num):
    bin_val = [""]
    while num >= 1:
        divide_by2 = num / 2
        divide_by2_rounded = num // 2
        if divide_by2 > divide_by2_rounded:
            bin_val.append("1")
        else:
            bin_val.append("0")
        num = num // 2

    return "".join(bin_val[::-1])


# print(easy_transform(number))
# print(" ", transform(number))

bin_number1 = 0b00100100
bin_number2 = 0b10011100
convert_to_decimal =  12 # 0 + 0 + 1 * 2^2 + 0 + 0 +2^5 (36)
input_from_user = input("enter a number: ")


def convert_to_int(binary):
    binary_to_str = str(binary)[::-1] # 001001
    counter = 0
    solution = 0
    for num in binary_to_str:
        if num == "1":
            solution = solution + 2 ** counter
        counter += 1
    return solution

print(convert_to_int(convert_to_decimal))


def to_decimal(bin_val):
    pass


sen = "You've always been crazy, this is just the first chance you've had to express yourself."
sen2 = "“I feel really awake. I don't recall ever feeling this awake."

print(bin_number2[::-1])
# print(transform(number))
