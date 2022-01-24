


def is_polinsrome(temp):
    return temp == temp[::-1]



str1 = "aabbaa"
str2 = "helloolleh"
str3 = "notpolindrome"

print(is_polinsrome(str1))
print(is_polinsrome(str3))
print(is_polinsrome(str2))

l1 = [1, 2 , 3 , 2, 1]
l2 = [1,2,3] # [3, 2, 1]

print(is_polinsrome(l1))
print(is_polinsrome(l2))

n1 = 1001

print(is_polinsrome(n1))
