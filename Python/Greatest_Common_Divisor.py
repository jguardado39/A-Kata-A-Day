# Modified: 04/11/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	https://www.codewars.com/kata/5500d54c2ebe0a8e8a0003fd

	Find the greatest common divisor of two positive 
	integers. The integers can be large, so you need 
	to find a clever solution.

	The inputs x and y are always greater or equal 
	to 1, so the the greatest common divisor will 
	always be an integer that is also greater or equal 
	to 1.

	"""
	def __init__(self):
		pass

	def mygcd(x, y):
		while(y):
			x, y = y, x % y
		return x

	def mygcd_alt(x,y):
	  return x if y == 0 else mygcd(y, x % y)

if __name__ == '__main__':
    sol = Solution()