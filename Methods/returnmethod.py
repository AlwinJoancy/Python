# Given two int values, return their sum. Unless the two values are the same, then return double their sum.
# sum_double(1, 2) → 3
# sum_double(3, 2) → 5
# sum_double(2, 2) → 8
def sum_double(a, b):
  if a==b:
    return 2*(a+b)
  else:
    return(a+b)
# Solution:
def sum_double(a, b):
  # Store the sum in a local variable
  sum = a + b
  
  # Double it if a and b are the same
  if a == b:
    sum = sum * 2
  return sum

# Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21.
# diff21(19) → 2
# diff21(10) → 11
# diff21(21) → 0

def diff21(n):
  if n <= 21:
    return 21 - n
  else:
    return (n - 21) * 2

We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.


parrot_trouble(True, 6) → True
parrot_trouble(True, 7) → False
parrot_trouble(False, 6) → False

def parrot_trouble(talking, hour):
  if talking and (hour<7 or hour>20):
    return True
  else:
    return False

Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.


makes10(9, 10) → True
makes10(9, 9) → False
makes10(1, 9) → True
def makes10(a, b):
  if (a==10 or b==10) or (a+b==10):
    return True   
  return False
  