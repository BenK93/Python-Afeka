class MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
Iterable = iter(myclass)

print(next(Iterable))
print(next(Iterable))
print(next(Iterable))
print(next(Iterable))
print(next(Iterable))
