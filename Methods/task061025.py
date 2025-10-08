def email(Name,Age):
    print(Name,Age,"@gmail.com")
email(Name="aa",Age=20)

def countA(msg):
    print("Given text: ",msg)
    x = msg.count("a")
    print("Total number of letter a present in the text is: ",x)
countA("Today is tuesday")

def hallowsquare(size):
    size=int(input("Enter the numer: "))
    if size<3:
        print("Enter the number greater 3")
    else:
         i=1
         while size<5

# def hallowsquare(size):
#         if size<3:
#         print("Enter size value greater than 3")
#         return
#     for row in range(size):
#         for col in range(size):
#            if row==0 or row==size-1 or col==0 or col==size-1:
#                print("*", end="")
#            else:
#                print(" ", end="")
#         print()       
# hallowsquare(3)               

