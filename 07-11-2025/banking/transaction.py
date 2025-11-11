class Transaction:
    def __init__(self,tId,tType,amount):
        self.__transactionId = tId
        self.__transactionType = tType
        self.__amount = amount

    def printTransaction(self):
        print(f"--Tr_No: {self.__transactionId}---Ttype: {self.__transactionType}--amount: {self.__amount}")