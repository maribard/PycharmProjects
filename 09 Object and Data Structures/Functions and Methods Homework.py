'''
import math


def vol(rad):
    return rad**3*math.pi*(4/3)

print(vol(2))
'''

'''
def up_low(s):
    u = 0
    l = 0
    for x in s:
        if x.isupper():
            u += 1
        else:
            if x.islower():
                l += 1
    print("No. of Upper case characters : {0}".format(u))
    print("No. of Lower case Characters : {0}".format(l))



s = 'Hello Mr. Rogers, how are you this fine Tuesday?'
up_low(s)'''


'''
def unique_list(lst):
    new_list = []
    for x in lst:
        if x in new_list:
            continue
        else:
            new_list.append(x)
    return new_list


print(unique_list([1,1,1,1,2,2,3,3,3,3,4,5]))'''



"""
def multiply(numbers):
    multi = 1
    for x in numbers:
        multi = multi*x
    return multi

print(multiply([1,2,3,-4]))
"""



'''
def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False



print(palindrome('heelleh'))'''



'''
import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    for x in alphabet:
        if x in str1:
            continue
        else:
            return False
    return True

print(ispangram("The quick brown fox jumps over the lazy dog"))'''