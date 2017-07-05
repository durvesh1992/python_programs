# Delete a vowel from a sentence

import sys

var1 = "San Jose State university"
var2 = list(var1)

# remove the vowels
for i in var2:
    if i in "aeiou":
        var2.remove(i)

print "String without vowels: ",''.join(var2)
