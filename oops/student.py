class student:
    Name = ""
    Age = ""
    Std = ""
    Sectn = ""
    Gender = ""
    Address = ""

    def stu(self, Name):
        print("Student Name", Name)

    def stdage(self, Age):
        print("Student age: ", Age)


s1 = student()
s1.Name = "AA"
s1.Age = 20
s1.Address = "Chennai"
print(s1.Name, s1.Age, s1.Address)

s2 = student()
s2.Name = "BB"
s2.Age = 22
s2.Address = "Pondy"
print(s2.Name, s2.Age, s2.Address)

s3 = student()
s3.Name = "CC"
s3.Age = 15
s3.Address = "Saram"
print(s3.Name, s3.Age, s3.Address)

s4 = student()
s4.Name = "DD"
s4.Age = 16
s4.Address = "Villupuram"
print(s4.Name, s4.Age, s4.Address)

s5 = student()
s5.Name = "BB"
s5.Age = 19
s5.Address = "Cuddalore"
print(s5.Name, s5.Age, s5.Address)
