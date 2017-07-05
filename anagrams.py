# Find anagrams
# 
# new file
import sys

# constant
CHAR = 256

#init the list
list1 = [0] * CHAR
list2 = [0] * CHAR

#Demo names for anagrams
name1 = "abhijeet"
name2 = "bhiteeja"

# name1 to list1
for i in range(len(name1)):
    list1[ord(name1[i])] += 1
#print list1

#name2 to list2
#for i in range(len(name2)):
    list2[ord(name2[i])] += 1

#print list2

# compare both the list
for i in range(len(list1)):
    if list1[i] != list2[i]:
        print "Not an anagram"
        sys.exit()

print "Anagrams"
