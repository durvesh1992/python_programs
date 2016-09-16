#Find max out of three num

# Function to find out the maximum number among 3 number
def max_three(n1,n2,n3):
    maxVal = n1
    if n2 > maxVal or n3 > maxVal:
        if n2 > n3:
            maxVal = n2
        else:
            maxVal = n3
    print "maxVal among three integers",maxVal

# Get three numbers from the user
num1 = input("Enter first Num")
num2 = input("Enter Second Num")
num3 = input("Enter Third Num")

# Call the function
max_three(num1, num2, num3)
