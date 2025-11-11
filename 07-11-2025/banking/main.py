

from bankAccount import BankAccount


b1 = BankAccount("mary","cust001")


print("options\n1)check balance\n2)deposit\n3)withdraw\n4)transactions")
while(True):
    option = int(input("press number: "))
    if(option==1):
        print(b1.checkBalance())
    elif option==2:
        amount = int(input("Enter the amount: "))
        b1.deposit(amount)
    elif option == 3:
        amount = int(input("Enter the amount: "))
        b1.withdraw(amount)
    elif option == 4:
        b1.getTransactions()