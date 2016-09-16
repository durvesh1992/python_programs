""" Reverse a Number"""
import sys

mynum = int(raw_input("Please Enter the number: "))
print "Your Number is: ",mynum

#if length of integer == 1, reverse is same
if(len(str(mynum)) == 1):
    print "Reverse of the number is: ",mynum
    sys.exit()

temp = mynum    
rev = 0

#looping till the temp is not equal to zero. Also, creating temp so that original value not lost
while(temp != 0):
    rev = rev*10
    rev = rev + temp % 10
    temp = temp / 10
print  "Reverse of the number is: ",rev    
