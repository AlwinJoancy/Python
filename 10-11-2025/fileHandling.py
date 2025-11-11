import json
#read file

def readFile(filename):
    file = open(filename,"r")
    return file.read()


# write file

def createNewFile(filename):
    file = open(filename,"x")
    file.write("hello this is filehandling clas")
    file.close()


def writeNewFile(filename,content):
    file = open(filename,"a")
    file.write(content)
    file.close()



writeNewFile("colors.txt","Red\nGreen\nOrange\nYellow\nblue\n----------------\n")

# print(readFile("students.txt"))


# command 
#  r - readfile
#  x - to create the new file if there exists same file name it throw an error
#  w - if there exists same filename it truncate and write the content
#  a - if there is existing content in the file it write with the new content to the file



# def writeStory():
#     fileName = input("Enter file name")
#     with open(fileName,"a") as file:
#         story = input("Enter the story: ")
#         file.write(story)

# writeStory()


def getDetailsFromCustomer():
    userCount = int(input("How many customer are in ? "))
    totalUsers = None
    try:
        fi = open("usrs.json","r")
        cont = fi.read()
        totalUsers = json.loads(cont)
        print(totalUsers)
        print(cont,"llllllllllllll")
    except FileNotFoundError as e:
        with open("usrs.json","x") as file:
            file.write("[]")



    for i in range(userCount):
        name = input(f"Enter the name for the customer {i+1}: ")
        age = input(f"Enter the gender for the customer {i+1}: ")
        address = input(f"Enter the address for the customer {i+1}: ")
        data = {"name":name,"age":age,"address":address}
        totalUsers.append(data)
    with open("usrs.json","w") as file:
        file.write(json.dumps(totalUsers,indent=2))
    
getDetailsFromCustomer()