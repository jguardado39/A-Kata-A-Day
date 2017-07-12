# Modified: 04/12/2017
#
# Author: jguardado39 (John Guardado)

class Solution(object):
	"""
	

	Write a function that takes an (unsigned) integer 
	as input, and returns the number of bits that are 
	equal to one in the binary representation of that 
	number.

	Example: The binary representation of 1234 is 
	10011010010, so the function should return 5 
	in this case

	"""
	def __init__(self, arg):
		super(Solution, self).__init__()
		self.arg = arg
		
	def countBits(n):
		sum = 0
		for i in [int(n) for n in '{0:0b}'.format(n)]:
			if i == 1:
				sum += 1
		return sum

	def countBits_alt(n):
    return bin(n).count("1")

if __name__ == '__main__':
    sol = Solution()