# Delete a vowel from a sentence

import sys

sent = "San Jose State university"
vowels = ['a','e','i','o','u']

# convert sentence to a list
consoList = list(sent)
print consoList

# remove the vowels from consoList
for i in consoList:
    if i in vowels:
        consoList.remove(i)

print "".join(consoList)
