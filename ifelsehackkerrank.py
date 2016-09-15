""" Task
Given an integer, , perform the following conditional actions:

    If is odd, print Weird
    If is even and in the inclusive range of to , print Not Weird
    If is even and in the inclusive range of to , print Weird
    If is even and greater than , print Not Weird

Input Format
A single line containing a positive integer, .

Constraints
Output Format
Print Weird if the number is weird; otherwise, print Not Weird.

Sample Input 0
3

Sample Output 0
Weird

Sample Input 1
24

Sample Output 1
Not Weird

Explanation

Sample Case 0:n = 3
n is odd and odd numbers are weird, so we print Weird.

Sample Case 1: n = 24
n > 20 and is even, so it isn't weird. Thus, we print Not Weird.

"""


#!/bin/python

import sys


N = int(raw_input().strip())
#print "Number obtained is: ",N

if N % 2 != 0:
    print "Wierd"
elif N > 20 and N % 2 == 0:
    print "Not Wierd"
elif N == 2 or N == 4:
    print "Not Wierd"
elif N <= 20 or N >= 6:
    print "Wierd"
