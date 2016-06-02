#Find odd or even using all different methods

#input the number of your choice
num=input("Enter a Number of your choice: ")
print "Your Number is: ",num

#Using Modulus Operator
if(num%2==0):
    print "Even number"
else:
    print "Odd Number"

#Without using Modulus or Bitwise Operator
if((num/2)*2==num):
    print "Even Number"
else:
    print "Odd number"

#Using Bitwise Operator
if (num&1==1):
    print "Odd Number"
else:
    print "Even Number"

#Using Conditional or ternary Operator
print "Even number " if num%2==0 else "Odd Number"


    
