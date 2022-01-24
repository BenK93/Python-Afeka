
list1 = []

for i in range(50):
    if i % 2 == 0:
        list1.append(i)
    else:
        list1.append(str(i))


print(list1)
l2 = []
for obj in list1:
    if obj == int(obj):
       l2.append(obj)

print(l2)
print(l2[4:200])
print(l2[::-1])