
class Calculate:
    # nonstatic member
    # non-static always depends on object
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)
    def sub(self):
        print(self.a-self.b)


def sayHi():
    print("hi........")