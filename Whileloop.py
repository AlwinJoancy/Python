# i = 1
# size = 5 
# while i <= size:
#     j = 1
#     while j <= size:
#         if i == 1 or i == size or j == 1 or j == size:
#             print("*", end=" ")
#         else:
#             print(" ", end=" ")
#         j += 1
#     print()
#     i += 1

i = 1
while i <= 5:
    j = 1
    while j <= i:
        print(j, end=" ")
        j += 1
    print()
    i += 1



