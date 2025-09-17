a=int(input("Enter a value =  "))
b=int(input("Enter b value =  "))
c=a+b
print(c)
print("=====Print the given number is Even or Odd Number=====")
Num=int(input("Enter the Number =  "))
if Num%2== 0:
    print("Given number is Even")
else:
    print("Given number is Odd")
print("====Program to check the number is Positive, Negative or Zero====")
Value=int(input("Enter a number: "))
if Value>0:
    print("Given number is Positive")
if Value<0:
    print("Given number is Negative")
else:
    print("Given number is Zero")
print("===Check a person is eligible to vote===")
Age=int(input("Enter your age: "))
if Age>=18:
    print("You are eligible to vote")
else:
    print("You are not eligible to vote")
print("====Check if the number is divisible by 5 and 11 or not====")
Number = int(input("Enter a number: "))
if Number%5==0 and Number%11==0:
    print("Given number divisible by 5 and 11")
else:
    print("Given number is not divisible by 5 and 11")
print("====Thank You====")