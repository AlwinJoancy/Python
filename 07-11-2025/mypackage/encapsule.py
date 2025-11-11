# encapsule -> wrapping the data into a single entity
# access specifier or modifier

# public protected private

# public - we dont need to mention in prefix
# protected - starts with the prefix _
# private - starts with the prefix __

class User:
    def __init__(self,username,password):
        self.__username = username
        self._password = password
    # getter
    def getUserName(self):
        return self.__username
    # setter
    def setUserName(self,uName):
        self.__username = uName


user = User("mary","mary123@")


print(user.getUserName())
user.setUserName("ocean")
print(user.getUserName())
user._password = "sda4f65"