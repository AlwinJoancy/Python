print("====Simple Calculator====")
n1 = int(input("Enter the first number = "))
n2 = int(input("Enter the second number = "))
print("Chose the operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

Choice = input("Enter your choice (+, -, *, %):")

match Choice:
    case"1":
        Result=n1+n2
        print(Result)
    case"2":
        Result=n1-n2
        print(Result)  
    case"3":
        Result=n1*n2
        print(Result)
    case"4":
        Result=n1%n2
        print(Result)
    case _:
     print("No such option")


