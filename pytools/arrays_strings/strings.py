# arrays_strings/strings.py
#
# Author: Daniel Clark, 2016

'''
This module contains functions to solve problems related to string
manipulation and testing
'''

def check_unique_chars(input_str):
    '''
    Function to check if string is composed of all unique characters

    Time complexity: O(n)

    Paramters
    ---------
    input_str : string
        input string to test for unique-ness

    Returns
    -------
    is_unique : boolean
        flag indicating whether string is unique or not
    '''

    # Import packages

    # Init variables
    chars_dict = {}
    is_unique = True

    # Check input type
    if not isinstance(input_str, str):
        err_msg = 'Input: %s is not string!' % str(input_str)
        raise TypeError(err_msg)

    # Iterate through string chars
    for char in input_str:
        if not chars_dict.has_key(char):
            chars_dict[char] = 1
        else:
            is_unique = False
            break

    # Return flag
    return is_unique

def check_unique_chars2(input_str):
    '''
    Function to check if string is composed of all unique characters
    using no other external data structures

    Time complexity: O(n^2)

    Paramters
    ---------
    input_str : string
        input string to test for unique-ness

    Returns
    -------
    is_unique : boolean
        flag indicating whether string is unique or not
    '''

    # Import packages

    # Init variables
    is_unique = True

    # Check input type
    if not isinstance(input_str, str):
        err_msg = 'Input: %s is not string!' % str(input_str)
        raise TypeError(err_msg)

    # Iterate through string chars
    for idx, char in enumerate(input_str):
        rest_of_str = input_str[idx+1:]
        if char in rest_of_str:
            is_unique = False
            break

    # Return flag
    return is_unique


def reverse_cstyle_str(input_str):
    '''
    Reverse a c-style string (ending in null char: '\0')
    '''

    # Import packges

    # Init variables
    str_length = len(input_str)-1 # Ignore null char
    rev_str = '\0'

    # Iterate through string from end to beginning
    for idx in range(str_length):
        rev_idx = str_length - idx - 1
        rev_char = input_str[rev_idx]
        rev_str = rev_str + rev_char

    # Return reversed string
    return rev_str