# Modified: 04/06/2017
#
# Author: jguardado39 (John Guardado)

class Solutions():
	"""
	Write a method, that will get an integer array 
	as parameter and will process every number 
	from this array.
	
	Return a new array with processing every 
	number of the input-array like this:

	If the number has an integer square root, take this, otherwise square the number.

	[4,3,9,7,2,1] -> [2,9,3,49,4,1]

	The input array will always contain only 
	positive numbers and will never be empty or 
	null.

	The input array should not be modified!

	"""
	def __init__(self):

	from math import sqrt
	def square_or_square_root(arr):
	    t = []
	    for x in arr:
	        if int(sqrt(x)) == x ** 0.5:
	            t.append(int(sqrt(x)))
	        else:
	            t.append(x*x)
	    return t

if __name__ == '__main__':
	sol = Solution()
