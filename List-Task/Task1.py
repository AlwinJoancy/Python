# string1 = ["green", "yellow","peacock","elephant"]
# longest=max(string1, key=len)  
# print("Longest string in the list is: ", longest) 

# long=""
# for i in string1:
#     if len(i)>len(long):
#        long=i
# print("Longest string in the list is: ", i)        


# b=("dsjflksd")
# l=len(b)
# print("Length of given string is :",l)

tuple1 = (43,65,21,46,77,83,2)
print("Tuple:", tuple1)
print("---converts tuple to list---")
ascend = list(tuple1)
print(ascend)
print("---sorting the elements in ascending order---")
ascend.sort()
print(ascend)
print("---Converts list to tuple---")
ctup=tuple(ascend)
print(ctup)
print("---Descending order---")
ascend.sort(reverse=True)
print(ascend)

