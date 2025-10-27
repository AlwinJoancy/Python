# a=str()
# if len(str)<=1:
#     return str
#   else:
#     return str[-1]+str[1:-1]+str[0]
# --------------------
# s=str("Hello")
# result = ""
# for i in range(len(s)):
#     result += s[:i+1]  # Slice the string from the beginning up to and including index i
# print (result)
# -------------------
# num=12365
# if 1 and 2 and 3 in num:
#     print(True)
# print(False)

# original_string = "Hello world"
# insert_string = "Python "
# insert_position = 6  # Index where you want to insert the string

# # Slice the original string into two parts
# first_part = original_string[:insert_position]
# second_part = original_string[insert_position:]

# # Concatenate the parts with the insert string in between
# new_string = first_part + insert_string + second_part

# print(new_string)

# def getdata(a,b="aaa",c="bbb"):
#     print(a,end="\n", sep="*")
#     print(a,end="_",sep="*")
#     print(a,end="_",sep="*")
# getdata("Hi Hello")
# print("Welcome \n to Ocean Accademy","Saram", sep="//")

# ------------
def sum_num(*data):
    return sum(data)
Sum=sum_num(10,20,30,23,11)
print("Total:", Sum)

# If you want to pass multiple numbers to the function without using *,
# you must pass them as a single iterable (like a list or tuple):
def sum_num(data):
    return sum(data)
Sum = sum_num([10, 20, 30, 23, 11])
print("Total:", Sum)
# ------------------------

# def remove_dup(sentence):
#     return " ".join(dict.fromkeys(sentence.split()))
# Text = "This is Ocean Accademy This."
# Answer = remove_dup(Text)
# print(Answer)



li=["hi","hello","hi"," ","hello","is"]
s = {}
result=[]
for i in li:
    s[i] = li.count(i)      
    if i not in result:
        result.append(i)
print(s)
print(result)
