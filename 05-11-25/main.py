# importing the entire module
# import calculate 
# importing class or method from a module
from calculate import Calculate as calc,sayHi


# example 1
# obj1 = calculate.Calculate(10,20)
# obj1.add()
# calculate.sayHi()


# example 2
obj2 = calc(20,18)
obj2.add()
obj2.sub()
sayHi()


from printer import starPrinter,linePrinter

# import printer

from printer.hashPrinter import HashPrinter

starPrinter.StarPrinter(20).makePrint()
HashPrinter(20).makePrint()
linePrinter.LinePrinter(20).makePrint()