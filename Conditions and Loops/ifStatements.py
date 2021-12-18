
string = "hello world"

if string is "hello world":
    print("Yes it is ", string)
else:
    print("Not it is not")

# same thing
if string == "hello world":
    print("Yes it is ", string)
else:
    print("Not it is not")

string2 = "BAD"

if string2.isupper():
    print("True")
else:
    print("False")

if "B" in string2:
    print("True")
else:
    print("False")
