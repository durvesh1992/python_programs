""" Hacker Rank leap year problem using functions"""


def is_leap(year):
    leap = False
    
    #print year
    if year % 400 == 0:
        leap = True
    elif year % 100 == 0:
        leap = False
    elif year % 4 == 0:
        leap = True
    else:
        leap = False
    # Write your logic here
    
    return leap
    
# Fetching the year from the user    
year = int(raw_input())
print is_leap(year)
