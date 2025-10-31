class Employee:
    def __init__(self, name, salary, department):
        self.name = name
        self.salary = salary
        self.department = department

    def getDetails(self):
        print(self.name)
        print(self.salary)
        print(self.department)


class Manager(Employee):
    def __init__(self, name, salary, department, teamSize):
        super().__init__(name, salary, department)
        self.teamSize = teamSize

    def getDetails(self):
        super().getDetails()
        print(self.teamSize)


class Developer(Employee):
    # def __init__(self, programmingLangauge):
    #     self.programmingLanguage = programmingLangauge

    def getDetails(self):
        # the below line call the parent method
        super().getDetails()
        print(self.programmingLanguage)

    def __init__(self, name, salary, department, pl):
        # the below line call the parent constructor
        super().__init__(name, salary, department)
        self.programmingLanguage = pl


d1 = Developer("mary joancy", 100000, "IT", "python FS")
m1 = Manager("Mary joancy", 500000, "Management", 10)

d1.getDetails()
print("===============")
m1.getDetails()
