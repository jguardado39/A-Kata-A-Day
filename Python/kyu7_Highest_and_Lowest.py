# Completed 04/05/2017
#
# author: jguardado39 (John Guardado)

class Solution():
	'''
	https://www.codewars.com/kata/highest-and-lowest/python
	
	In this little assigment you are given a string of

	space separted numbers, and have to return the

	hightest and lowest number.

	# For example 

	high_and_low("1 2 3 4 5")  # return "5 1"
	
	high_and_low("1 2 -3 4 5") # return "5 -3"
	
	high_and_low("1 9 3 4 -5") # return "9 -5"
	'''
	def __init__(self):
		pass

	def high_and_low(numbers):
		lst = [int(s) for s in numbers.split()]
		high, low, count = lst[0], lst[0], 1
		while count < len(lst):
			if lst[count] > high:
				high = lst[count]
				count += 1
			elif lst[count] < low:
				low = lst[count]
				count += 1
			else:
				count += 1
		return ' '.join(map (str, [high, low]))