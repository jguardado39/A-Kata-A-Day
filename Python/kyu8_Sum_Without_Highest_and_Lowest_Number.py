# Modified: 04/11/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	https://www.codewars.com/kata/sum-without-highest-and-lowest-number
	
	Sum all the numbers of the array (in F# and 
	Haskell you get a list) except the highest and 
	the lowest element (the value, not the index!).
	(The highest/lowest element is respectively 
	only one element at each edge, even if there 
	are more than one with the same value!)

	Example:
	
	{ 6, 2, 1, 8, 10 } => 16
	{ 1, 1, 11, 2, 3 } => 6

	If array is empty, null or None, or if only 1 
	Element exists, return 0.

	"""
	def __iniit__(self):
		pass

	def sum_array(arr):
	    if arr == None:
	        return 0
	    elif len(arr) <= 2:
	        return 0
	    else:
	        arr.remove(min(arr)), arr.remove(max(arr))
	        return sum(arr)

   def sum_array_alt(arr):
   		return sum(sorted(arr)[1:-1]) if arr and len(arr) > 1 else 0

if __name__ == '__main__':
    sol = Solution()
