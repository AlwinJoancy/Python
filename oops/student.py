class Student:
    # Use camel case to declare variables
    name = ""
    age = ""
    std = ""
    sectn = ""
    gender = ""
    address = ""

    def setName(self, name):
        # self.name - is called object refered name
        # name - is an argument get from function/method
        self.name=name
        print("Student1 name: ", name)

    def setAge(self, age):
        self.age=age
        print("Student1 age: ", age)


s1 = Student()
s1.setName("AA")
s1.setAge(20)
s1.address = "Chennai"
print("Student1 address:", s1.address)


s2 = Student()
s2.name = "BB"
s2.age = 22
s2.address = "Pondy"
print(s2.name, s2.age, s2.address)

s3 = Student()
s3.name = "CC"
s3.age = 15
s3.address = "Saram"
print(s3.name, s3.age, s3.address)

s4 = Student()
s4.name = "DD"
s4.age = 16
s4.address = "Villupuram"
print(s4.name, s4.age, s4.address)

s5 = Student()
s5.name = "BB"
s5.age = 19
s5.address = "Cuddalore"
print(s5.name, s5.age, s5.address)
