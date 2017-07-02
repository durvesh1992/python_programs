"""Assume a random list of integer numbers and extract a list from the input list in such a way that their sum is maximum and also no two numbers in the output list are adjacent
example:
input: [1,3,56,78,92,7,8,160,150]

output: [160,92,56,1] """

#Test Cases
a = [1, 3, 56, 78, 92, 7, 8, 160, 150]
#a = [56, 3, 0]
#a = [1,4,56]
# a = [57,58,56]
#a = []
#a = [1]

# List to store output
oplist = []

# Iterate through the list
while len(a) > 1:
    maxval = max(a)
    oplist.append(maxval)

    # Append the max Value in the output list and
    #  remove the original elements
    myindex = a.index(maxval)
    if myindex + 1 <= len(a) - 1 :
        a.remove(a[myindex + 1])

    if myindex - 1 >= 0  :
        a.remove(a[myindex - 1])

    a.remove(maxval)

if len(a) > 0:
    oplist.append(a[0])
print "Output list: ", oplist
