class Course():
    title=""
    duration=""
    
    def __init__(self, title, duration):
      self.title = title
      self.duration = duration

class FreeCourse(Course):
    def __init__(self):
      self.showadd()

    def showadd(self):
      print("Advertaisment")
class Paidcourse(Course):
    def __init__(self, price):
      self.price = price
    def applydiscount(self,discount):
      self.price%discount=discount
                 