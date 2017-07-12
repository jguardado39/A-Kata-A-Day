# Modified: 04/06/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	https://www.codewars.com/kata/5467e4d82edf8bbf40000155

	Your task is to make a function that can take any 
	non-negative integer as a argument and return it 
	with it's digits in descending order. Essentially, 
	rearrange the digits to create the highest 
	possible number.

	Examples:

	Input: 21445 Output: 54421

	Input: 145263 Output: 654321

	Input: 1254859723 Output: 9875543221

	"""
	def __iniit__(self):
		pass

	def Descending_Order(num):
	    return int(''.join(sorted(str(num), reverse = True)))

	def Descending_Order_alt(num):
    return int(''.join(sorted(str(num))[::-1]))

if __name__ == '__main__'
	sol = Solution()