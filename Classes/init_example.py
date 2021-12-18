class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name,
              " and i am " + self.age + " years old")


p1 = Person("John", 36)
p1.myfunc()
p1.age = 10
p1.name = 'ben'
p1.myfunc()
