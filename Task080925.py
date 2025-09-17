#print("===Numbers from 1 to 20 in single line===")
#for i in range(1,21,1):
#    print(i, end=" ")
    
print("===20 to 1 in single line seprated by - ===")
for n in range(20,0,-1):
    print(n, end="-")
print("===Cube of numbers from 1 to 10===")
for c in range(1,11):
    c=c*c*c
    print(c, end=" ")
print("===Number from 1 to 10 in reverse order===")
for rev in range(10,0,-1):
    print(rev, end=" ")
print("===Number ends with 7===")
for num in range(1,101):
    if num%10==7:
     print(num, end=" ")

