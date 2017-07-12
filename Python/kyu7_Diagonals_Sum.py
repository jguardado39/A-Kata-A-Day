# Modififed: 04/11/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	https://www.codewars.com/kata/5592fc599a7f40adac0000a8/

	Create a function that receives a (square) matrix 
	and calculates the sum of both diagonals (main 
	and secondary)

	Matrix = array of n length whose 
	elements are n length arrays of integers.

	3x3 example:

	sum_diagonals[
	  [ 1, 2, 3 ],
	  [ 4, 5, 6 ],
	  [ 7, 8, 9 ]
	  ] ) == 30 # 1 + 5 + 9 + 3 + 5 + 7
	
	"""
	def __init__(self):
		pass

	def sum_diagonals(matrix):
	    result1, result2 = 0, 0
	    for i, row in enumerate(matrix):
	        result1 += row[i]
	        result2 += row[-i + (len(matrix) - 1)]
	    return result1 + result2

    def sum_diagonals_alt(matrix):
    return sum(r[i]+r[-1-i] for i, r in enumerate(matrix))

if __name__ == '__main__'
	sol = Solution()