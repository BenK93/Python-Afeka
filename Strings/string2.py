
def is_polinsrome(string):
    return string == string[::-1]


str1 = "aabbaa"
str2 = "helloolleh"
str3 = "notpolindrome"

print(is_polinsrome(str1))
print(is_polinsrome(str2))
print(is_polinsrome(str3))
