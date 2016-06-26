# coding=utf-8
# !/usr/bin/python

def printMax(first_number, second_number):
	'''Return the maximum of two numbers.

	The two numbers must be integers.
	'''
	first_integer_number = int(first_number)
	second_integer_number = int(second_number)

	if first_integer_number > second_integer_number:
		return first_integer_number
	else:
		return second_integer_number


print printMax.__doc__