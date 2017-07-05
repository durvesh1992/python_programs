# Delete a vowel from a sentence

import sys

var1 = "San Jose State university"
var2 = ""

# remove the vowels
for i in var1:
    if i in "aeiou":
        continue
    else:
        var2 += i

print "String without vowels: ",var2
