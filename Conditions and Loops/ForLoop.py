
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
    print("i=", i," ", word, " = ", strings[i])

l1 = [12,3,33,100]

# for num in l1:
#     print(num)
#
# for index, num in enumerate(l1):
#     print(index, num)

print(type(range(100)))
# third example - break statement
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
    if x == "banana":
        break
