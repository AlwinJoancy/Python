from abstraction import Triangle,Circle
class Demo():
    def __init__(self,shape):
        self.shape = shape


d = Demo(Triangle())
d.shape.calculatePerimeter()

