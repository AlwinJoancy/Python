class Student:
    schlName = ""
    standard = ""
    section = ""

    def __init__(self, name, standard, section):
        self.name = name
        self.standard = standard
        self.section = section


s1 = Student("A1", "10th", "A")
s1.name = "AA"
print(s1.name)
print(Student.name)
print(id(Student.name))
print(id(s1.name))


# print(p1.name)
# print(Person.name)
# print(id(p1.name), id(Person.name))
# p1.schoolname = "Private School"
# print(id(p1.schoolname), id(p2.schoolname))
# print(p1.schoolname, p2.schoolname)
