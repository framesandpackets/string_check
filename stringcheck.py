#!/usr/bin/env python

import re		#importing regex module
import header as welcome		#import module from local dir

welcome.greeting()		#calling welcome/landing module

string = input("\n Enter string you would like to check: ")   #calls for user input of string

print ("-------------------------------------------------------------")

def string_checker():		#string checker function
	quote_match = re.findall('"([^"]*)"',string)	#regex pattern for double quotes and text between quotes
	is_match = bool(quote_match)		#returns boolean value for regex call
	num_range = re.match(r'[0-9][0-2]', string)      #regex match pattern for intergers in range 1-12 in string using groupings
	bool_num = bool(num_range)
	pattern = re.compile(r'[.]$')		#compiling/loading regular expression for fullstop at end of string
	matched_fullstop = pattern.finditer(string)		#findering iterations of regex pattern above
	bool_fullstop = bool(matched_fullstop)
	if string[0].isupper(): 		#checking string for capital at start
		print("Test Passed: Captial letter used at start of string")
	else:
		print("Test Failed: Captial letter not used at start of string")
	if string[-1] == ".":
		print("\nTest Passed: You have used a fullstop at the end of string")
	else:
		print("\nTest Failed: You string does end with a fullstop")
	if is_match == True:
		print("\nYour string uses double quotation marks")
	else:
		print("\nYour string is not using double quotation marks")
	if bool_num == True:
		print("\nTest Failed: You have numbers below 13 that are not spelled out")
	else:
		print("\nTest Passed: All numbers below 13 have been spelled out")
string_checker()     #calling function

print("--------------------------------------------------------------")
