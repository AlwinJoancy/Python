print("====Nested for loop escape character====")
print("Hello \nWorld")
print("Welcome \tto \"India\"")
print("\\How are you \'pondicherry\' pondy i\bbeach")
print("\rbid bit")
for i in range(5):
    for j in range(6):
        print(i,j)
    print("===",i)