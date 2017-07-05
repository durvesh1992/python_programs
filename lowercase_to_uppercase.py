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

        if i in 'qwertyuiopasdfghjklzxcvbnm':
            upperCaseWord += chr(ord(i) - 32)
        else:
            upperCaseWord += i

    return upperCaseWord


mystr = "San jose state university"

print lower_to_upper(mystr)
print lower_to_upper_ascii(mystr)
