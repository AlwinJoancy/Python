mylist=[5,78,43,55,12,55,78,90]
li=[]
for i in range(len(mylist)):
    # print(i)
    num=mylist[i]
    occ=mylist.count(num)
    if occ>1:
        li.append(i)
print("Index of duplicate elements in the list: ", li)   

#   if mylist[i] % 2 == 0:
#      li.append(mylist[i])
# print("Even numbers in the given list:", li)       