from colorabstract import bgcolour 

class Paint():
    def __init__(self,painting):
        self.color = painting


bg = Paint(bgcolour())
bg.color.colortype()