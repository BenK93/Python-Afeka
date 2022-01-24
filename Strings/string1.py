string = "hello world"
string2 = "hello world what is going on"

print(string[len(string) // 2])


print(string[0:5])

print(string[5:11])

# example for loop of letters
for letter in string2:
    print(letter)


# example for loop of words
for word in string2.split(" "):
    print(word)


for word1, word2, in zip(string.split(" "), string2.split(" ")):
    print(word1)
    print(word2)



print(string[4:100])
