class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, class_name, grade_avg):
        Person.__init__(self, fname, lname)
        self.class_name = class_name
        self.grade_avg = grade_avg

    def __str__(self):
        return self.class_name + ' ' + self.grade_avg \
            + ' ' + self.firstname + ' ' + self.lastname


student = Student("Mike", "Tyson", "Yud-beit", "88")
student.printname()
print(student)


class Student2(Person):
    def __init__(self, fname, lname, class_name, grade_avg):
        super().__init__(fname, lname)
        self.class_name = class_name
        self.grade_avg = grade_avg

    def __str__(self):
        return self.class_name + ' ' + self.grade_avg \
            + ' ' + self.firstname + ' ' + self.lastname


student2 = Student("Mike", "Tyson", "Yud-beit", "88")
student2.printname()
print(student2)
