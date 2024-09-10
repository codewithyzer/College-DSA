from array import *
from typing import List

numbers = array('i', [6, 1, 2, 11, 3, 4, 5])

def find_largest(array_param):
    current = array_param[0]
    for element in array_param[1:]:
        if element > current:
            current = element
    return current

print('Given array:', numbers)
print('The largest number in the array:', find_largest(numbers))