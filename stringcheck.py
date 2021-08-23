#!/usr/bin/env python

import re

def caps_check(string):         #function to check first character in string in captial
    if string[0].isupper():
        return "Test Passed"
    else:
        return "Test Failed"

def period_check(string):       #function to check last element in string is '.'
    if string[-1] == '.':
        return "Test Passed"
    else:
        return "Test Failed"

def misplaced_period_check(string):     #function to check string for '.' from start to second last character
    if "." in string[0:-2]:
        return "Test Failed"
    else:
        return "Test Passed"

def number_check(string):  #function to number in string <= 12
    num_range = re.search(r'\d+', string) #regex search for one or more digits in string
    bool_num = bool(num_range)     #True/False return on regex search
    if num_range == None:
        return "Test Passed"
    if bool_num == True:
        num_int = int(string[num_range.start():num_range.end()])       #parsing regex return and returning integer value
        match_int = int(num_int)
        if match_int <= 12:
            return "Test Failed"
        else:
            return "Test Passed"

def quote_check(string):
    quote_count = string.count('''"''')        # count the amount of quote marks in string
    modulo_check = quote_count % 2           # find if diving the count by 2 has a remainder
    if modulo_check != 0:
        return("Test Failed")
    else:
        return("Test Passed")
