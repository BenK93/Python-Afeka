

username = ""
password = ""
counter = 0

while username != "student" or password != "aaa":
    if counter < 3:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
    else:
        break
    if counter > 0:
        print("wrong username/password, try again")
    counter += 1

if username == "student" and password == "aaa":
    print("you entered the enchanted palace")
else:
    print("wrong username/password, contact a system administrator")

















