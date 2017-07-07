# Find Anagram using sorted function python
import sys

#demo names for list
d = {'apple': [10,9,8], 'banana': [99,88,77], 'peachasd': [122,556,143]}

# Sort Values
for item in d:
    d[item].sort()
    print item,":",d[item]

# Sort keys
for item in sorted(d, key = d.get):
    print item,":",d[item]


# max item
print "Max: ",max(d, key = d.get)
