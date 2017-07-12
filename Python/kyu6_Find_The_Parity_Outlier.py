# Modified: 04/12/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""

	You are given an array (which will have a length 
	of at least 3, but could be very large) containing 
	integers. The array is either entirely comprised 
	of odd integers or entirely comprised of even 
	integers except for a single integer N. Write a 
	method that takes the array as an argument and 
	returns N.

	For example:

	[2, 4, 0, 100, 4, 11, 2602, 36]

	Should return: 11

	[160, 3, 1719, 19, 11, 13, -21]

	Should return: 160

	"""

	def __init__(self):
		pass

	def find_outlier(integers):
		odd, even = [], []
		for i in integers:
			if i % 2 == 0:
				even.append(i)
			else:
				odd.append(i)
		if len(even) == 1:
			return even[0]
		return odd[0]

	def find_outlier_alt(integers):
    	parity = [n % 2 for n in integers]
    	return integers[parity.index(1)] if sum(parity) == 1 else integers[parity.index(0)]

if __name__ == '__main__':
    sol = Solution()