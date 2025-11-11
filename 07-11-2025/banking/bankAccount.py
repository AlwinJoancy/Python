from transaction import Transaction 
class BankAccount:
   
    def __init__(self,name,customerId):
        self.name = name
        self.customerId = customerId
        self.__balance = 0
        self._ifscCode = "IFSC10123"
        self.transactions = []
        self.tId = 0
    
    def deposit(self,amount):
        if(amount<0):
            print("please give the correct amount")
            return
        self.tId = self.tId+1
        self.transactions.append(Transaction(self.tId,"credited",amount))
        self.__balance += amount
    
    def withdraw(self,amount):
        if(self.__balance>amount):
            self.__balance -= amount
            self.tId = self.tId+1
            self.transactions.append(Transaction(self.tId,"debited",amount))
            print(f"your amount is debited rs{amount}")
        else:
            print("insufficient balance")

    def checkBalance(self):
        return self.__balance

    def getTransactions(self):
        for transaction in self.transactions:
            transaction.printTransaction()
        print(f"-------- balance is {self.__balance}")