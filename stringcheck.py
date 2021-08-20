#!/usr/bin/env python

import re		#importing regex module
import header as welcome		#import module from local dir

welcome.greeting()		#calling welcome/landing module

string = input("\n Enter string you would like to check: ")   #calls for user input of string

print ("-------------------------------------------------------------")

def string_checker():		#string checker function
	quote_match = re.match(r'"\w+"',string)	#regex pattern for double quotes and text between quotes
	is_match = bool(quote_match)		#returns boolean value for regex call
	num_range = re.match(r'[0-9][0-2]', string)      #regex match pattern for intergers in range 1-12 in string using groupings
	bool_num = bool(num_range)
	if string[0].isupper(): 		#checking string for capital at start
		print("Test Passed: Captial letter used at start of string")
	else:
		print("Test Failed: Captial letter not used at start of string")

	if string[-1] == ".":
		print("\nTest Passed: You have used a fullstop at the end of string")
	else:
		print("\nTest Failed: You string does end with a fullstop")

	if is_match == True:
		print("\nTest Passed: You have used double quotes in your string")
	else:
		print("\nTest Failed: You have not used double quotes in your string")

	if bool_num == True:
		print("\nTest Failed: You have numbers below 13 that are not spelled out")
	else:
		print("\nTest Passed: All numbers below 13 have been spelled out")
	if "." in string[0:-2]:
		print("\nTest Failed: You have used a full stop somewhere other than end of the string")

string_checker()     #calling function

print("--------------------------------------------------------------")
