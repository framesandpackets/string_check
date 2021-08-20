#!/usr/bin/env python

import re		#importing regex module
import header as welcome		#import module from local dir

welcome()		#calling welcome/landing module

string = input("\n Enter string you would like to check: ")   #calls for user input of string

print ("-------------------------------------------------------------")

def string_checker():		#string checker function
	quote_match = re.findall('"([^"]*)"',string)	#regex pattern for double quotes and text between quotes
	is_match = bool(quote_match)		#returns boolean value for regex call
	num_range = re.findall('[0-13]', string)      #regex pattern for intergers in range 1-13 in string
	matched_num = bool(num_range)
	if string[0].isupper() and string[-1] == ".":		#checking string for capital at start and period character "." at end
		print("Your string has passed test for captial letter at start and trailing '.'")
	else:
		print("Your string does not meet our criteria for captials and full stops")
	if matched_num == True:
		print("\nYour string includes numbers below 13 that are not spelled out")
	else:
		print("\nYour string meets our criteria for numbers")
	if is_match == True:
		print("\nYour string uses double quotation marks")
	else:
		print("\nYour string is not using double quotation marks")
	if string[-1] != ".":		#checking for period anywhere but at the end on the string
		print("\nYou have used a period character in the string somewhere other than finishing the sentence")

string_checker()     #calling function

print("--------------------------------------------------------------")
