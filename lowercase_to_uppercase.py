"""
Lower case to upper case

I/p = san jose state university

O/p = SAN JOSE STATE UNIVERSITY
"""

import sys


def lower_to_upper(mystr):
    return mystr.upper()

def lower_to_upper_ascii(mystr):
    upperCaseWord = ""
    for i in mystr:
        #print "i = " + i + "and Asci value = " +str(ord(i))

        if i == " ":
            upperCaseWord += " "

        j = ord(i) - 32
        upperCaseWord += chr(j)

    return upperCaseWord


mystr = "san jose state university"

print lower_to_upper(mystr)
print lower_to_upper_ascii(mystr)
