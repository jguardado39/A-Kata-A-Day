# Modified: 04/11/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	Write a program that finds the summation of every number between 1 and num. The number will always be a positive integer greater than 0.

	For example:

	summation(2) -> 3
	1 + 2

	summation(8) -> 36
	1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

	"""
	def __init__(self):
		pass

	def summation(num):
	    return (num * (num + 1)) / 2

    def summation_alt(num):
    	return sum(xrange(num + 1))

if __name__ == '__main__':
    sol = Solution()