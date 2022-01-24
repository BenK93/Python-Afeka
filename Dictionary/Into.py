

thisdict = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}


print(thisdict)
print(thisdict["brand"])
print(len(thisdict))


print("--------------------")
thisdict["year"] = 2018
thisdict['my_key'] = [1,2,3,4,5, "100", "hello world"]
print(thisdict)

thisdict.update({"model": "Ferari"})
print("--------------------")
print(thisdict)

thisdict2 = {
    "brand": "Ford",
    "electric": False,
    "year": 1964,
    "colors": ["red", "white", "blue"]
}
print(type(thisdict2))

for key, value in thisdict.items():
    print("Key = ", key, ", Value = ", value)

print("--------------------")
for key, value in thisdict2.items():
    print("Key = ", key, ", Value = ", value)

print("starting in here--------------------")

for item in thisdict:
    print("Key = ", item, ", Value = ", thisdict[item])


print('ending here--------')
for key in thisdict2.keys():
    print("Key = ", key)

for value in thisdict2.values():
    print("value = ", value)

l1 = [1,2 , 3]
l2 = ["string1", "string2", "string3"]

d1 = {x : y for x, y in zip(l1,l2)}

for l1_item, l2_item in zip(l1,l2):
    d1[str(l1_item)] = l2_item


print(d1)

example = [str(i) for i in range(50) if i % 2 == 0 and i > 10]
print(example)
