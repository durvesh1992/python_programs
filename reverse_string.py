"""

Reverse a Strng
I/p = durvesh
O/p = hsevrud

"""

import sys

# Function to reverse a string
def reverse_string(s):
    reverse = ''
    for i in range(len(s)):
        reverse += s[len(s) - i - 1]
    return reverse

mystr = "durvesh"

# Python string reverse shortcut
print mystr[::-1]

# call the function to reverse the string
print reverse_string(mystr)
