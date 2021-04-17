import re

lineone = input("Enter first value\n")
linetwo = input("Enter second value\n")

#got input, now get the numbers out

A = [int(s) for s in re.findall(r'\d+', lineone)]
B = [int(s) for s in re.findall(r'\d+', linetwo)]


#we want to find overlap, which is when either endpoint of B is between the endpoints of A

if (A[0] <= B[0] <= A[1]) or (A[0] <= B[1] <= A[1]):
    print("Overlap")
else:
    print("Not overlap")
