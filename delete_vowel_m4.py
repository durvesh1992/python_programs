# Delete a vowel from a sentence

import sys

var1 = "San Jose State university"

# remove the vowels
for i in var1:
    if i in 'aieou':
        var1 = var1.replace(i,'')
print "String without vowels: ",var1
