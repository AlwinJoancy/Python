# class -> data
# data members => properties, methods
# noun -> properties eg, name,address,age
# verbs -> methods eg, printStudent, getName, setAddress


class Phone:
    color = ""
    numpad = ""
    brandName = ""
    displayType = ""
    simSlotCount = 0

    def call(self, phNumber):
        print("calling..........", phNumber)

    def torchOn(self):
        print("torchOn")

    def switchOff(self):
        print("phone is off")


p1 = Phone()

p1.color = "green"
print(p1.color)
print(p1.numpad)
print(p1.brandName)
print(p1.displayType)
print(p1.simSlotCount)
p1.call(56141453417521352)
p1.torchOn()
p1.switchOff()
p2 = Phone()
print(id(p1))
print(id(p2))
