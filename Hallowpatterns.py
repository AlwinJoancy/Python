rows = 5

for i in range(rows):
    for j in range(rows - i - 1):
        print(" ", end=" ")

    
for k in range(2 * i + 1):
        if k == 0 or k == 2 * i:
    
            print("*", end="")
        elif i == rows - 1 and k % 2 == 0:
       
            print("*", end="")
        else:
       
            print(" ", end="")
print()