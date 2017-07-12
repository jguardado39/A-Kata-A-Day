# Modified: 04/06/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	https://www.codewars.com/kata/573d498eb90ccf20a000002a/
	
	Fans of The Wire will appreciate this one. For 
	those that haven't seen the show, the 
	Barksdale Organization has a simple method 
	for encoding telephone numbers exchanged via 
	pagers: "Jump to the other side of the 5 on the 
	keypad, and swap 5's and 0's."

	Here's a keypad for visualization.

	┌───┬───┬───┐
	│ 1 │ 2 │ 3 │
	├───┼───┼───┤
	│ 4 │ 5 │ 6 │
	├───┼───┼───┤
	│ 7 │ 8 │ 9 │
	└───┼───┼───┘
	    │ 0 │
	    └───┘
	
	Detective, we're hot on their trail! We have a 
	big pile of encoded messages here to use as 
	evidence, but it would take way too long to 
	decode by hand. Could you write a program to
	do this for us?

	Write a funciton called decode(). Given an 
	encoded string, return the actual phone 
	number in string form. Don't worry about input 
	validation, parenthesies, or hyphens.

	# For example

	decode("4103432323"), "6957678787"
	decode("4103438970"), "6957672135"
	decode("4104305768"), "6956750342"
	decode("4102204351"), "6958856709"
	decode("4107056043"), "6953504567"
	"""
	def __init__(self):
		pass

	def decode(string):
		numbers = [int(string) for string in string]
		code = []
		for i in numbers:
			if i == 0:
				code.append(5)
			elif i == 5:
				code.append(0)
			else:
				code.append(10 - i)
		return ''.join(str(e) for e in code)

if __name__ == '__main__':
	sol = Solution()