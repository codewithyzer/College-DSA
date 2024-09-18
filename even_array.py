from array import *
from typing import List

def even_type_array(array_param):
    even_array = array('i', [])
    if len(array_param) >= 1:
        for element in array_param:
            if element % 2 == 0:
                even_array.append(element)
        return even_array
    else:
        return f'Error: Invalid array.\n{even_array}'
    
def even_type_list(given_list: List[int]) -> List[int]:
    even_array = []
    if len(given_list) >= 1:
        even_array = list(filter(lambda x: x % 2 == 0, given_list))
        return even_array
    else:
        return f'Error: Invalid array.\n{even_array}'
        
given_array = array('i', [i for i in range(1, 11)])
print('Given array:', given_array)
print(f'Result: {even_type_array(given_array)}')

print('')

python_list = [i for i in range(1, 11)]
print('Given list:', python_list)
print(f'Result: {even_type_list(python_list)}')


