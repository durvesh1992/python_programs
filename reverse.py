""" Reverse a Number"""
import sys

mynum=int(raw_input("Please Enter the number: "))
print "Your Number is: ",mynum

print "Number of digits: ",len(str(mynum))
if(len(str(mynum))==1):
    print "Reverse of the number is: ",mynum
    sys.exit()

temp=mynum    
rev=0
while(temp!=0):
    rev=rev*10
    rev=rev+temp%10
    temp=temp/10
print  "Reverse of the number is: ",rev    
