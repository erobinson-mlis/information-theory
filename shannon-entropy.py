# shannon-entropy.py
# calculates Shannon Entropy of a given a binary string

import math


#def shannon_entropy(x):
#    entropy = 0
#    entropy = 
#
#    return entropy


def binary_string_check(string):

    ''' accepts a string and returns True if the string is composed only of 0s and 1s'''

    list = [x for x in string]
    not_binary = []

    for i in list:
        if (i != '0' and i != '1'):
            not_binary.append(i)
            is_binary = False
        else:
            is_binary = True
            continue

    return is_binary


def shannon_entropy(string):

    '''Accepts a string (or maybe a list) and calculates the total entropy of the string.'''
    
    list = [x for x in string]
    
    for i in list:
        H = (0.5 * math.log(2,2)) * len(list)
    
    return H


string = input(f"Please enter a binary string of digits (0s and 1s only): ")

if binary_string_check(string) == False:
    print("This string contains something that is not a 0 or 1.")

if binary_string_check(string) == True:
    print("This string contains only 0s and 1s. Proceed")

shannon_entropy(string)
print(f"The Shannon entropy of {string} is H = {shannon_entropy(string)}")



