# print one to 100 without looping
import sys

# function defined for recursion
def printNum(i):
    print "Number : ",i
    if i < 100:
        printNum(i+1)

# init the number or take from the user
i = 1
printNum(i)
