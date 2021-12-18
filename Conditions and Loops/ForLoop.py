
arr = []
for i in range(10):
    arr.append(i)
print(arr)
#  second example
arr = []
for i in range(5, 100, 10):
    arr.append(i)
print(arr)

strings = ["h", "b", "c", "d", "e", "xc", "ggg"]
for word in strings:
    print(word)

for i, word in enumerate(strings):
    print(word, " = ", strings[i])

# third example - break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
