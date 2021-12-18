string = "hello world"
string2 = "hello world what is going on"

print(string[0:5])

print(string[5:11])

# example for loop of letters
for letter in string2:
    print(letter)
# example for loop of words
for word in string2.split(" "):
    print(word)

print(string[4:100])
