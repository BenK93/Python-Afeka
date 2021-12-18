
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
print("--------------------")

for key in thisdict2.keys():
    print("Key = ", key)

for value in thisdict2.values():
    print("value = ", value)
