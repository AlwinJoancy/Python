class Person:
    name = ""
    age = ""
    gender = ""
    dob = ""
    contact = ""
    bloodgroup = ""
    schoolname="Govt.school"

    def __init__(self, name, age, gender, dob, contact, bloodgroup):
        self.name = name
        self.age = age
        self.gender = gender
        self.dob = dob
        self.contact = contact
        self.bloodgroup = bloodgroup


p1 = Person("A1", 10, "male", 10 - 9 - 2003, 436347, "Ab-")
# p1.name = "A1"
# p1.age = 14
# p1.gender = "female"
# p1.dob = 12 - 12 - 2000
# p1.contact = 12345
# p1.contact = "A+"
p2 = Person("A2", 10, "male", 10 - 9 - 2003, 436347, "Ab-")
p3 = Person("A3", 23, "male", 12 - 6 - 2002, 9684565, "b+")
p4 = Person("A4", 18, "female", 3 - 11 - 2006, 5154454, "A-")
p5 = Person("A5", 20, "male", 7 - 3 - 2001, 967979769, "b-")

print(p1.name)
print(p2.age)
print(Person.name)
print(id(p1.name), id(Person.name))
p1.schoolname="Private School"
print(id(p1.schoolname), id(p2.schoolname))
print(p1.schoolname, p2.schoolname)
