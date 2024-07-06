# shannon-entropy.py
# calculates Shannon Entropy of a given a binary string



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


string = input(f"Please enter a binary string of digits (0s and 1s only): ")

if binary_string_check(string) == True:
    print("This string contains only 0s and 1s. Proceed")
if binary_string_check(string) == False:
    print("This string contains something that is not a 0 or 1.")





