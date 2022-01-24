to_convert = "hello world again"

# to_convert = to_convert.upper()
print(to_convert)

# returning true if all characters is upper case
if to_convert.isupper():
    print("True")
elif not to_convert.isupper():
    to_convert = to_convert.upper()


print(to_convert)

# print(to_convert.join("ABC"))

to_convert = to_convert.lower()
print(to_convert)
