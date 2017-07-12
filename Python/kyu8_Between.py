# Modified: 04/06/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""

	Write a function taking two parameters and 
	returning an int array of all elements between 
	the input parameters and including them.

	>>> between(1,4)
	>>> [1,2,3,4]

	"""
	def __init__(self):
		pass



	def between(a,b):
		between = [i for i in range(a,b+1)]
		return between

	def between_alt(a,b):
		return range(a, b + 1)	

if __name__ == '__main__':
	sol = Solution()