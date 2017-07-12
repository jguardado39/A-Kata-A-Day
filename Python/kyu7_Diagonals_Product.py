# Modififed: 04/11/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	https://www.codewars.com/kata/551204b7509063d9ba000b45

	Given a list of rows of a square matrix, find the 
	product of the main diagonal.

	Examples:

	main_diagonal_product([[1,0],[0,1]]) => 1

	main_diagonal_product([[1,2,3],[4,5,6],[7,8,9]]) => 45

	"""
	def __init__(self):
		pass

	def main_diagonal_product(mat):
		result = 1
		for i, row in enumerate(mat):
			result *= row[i]
		return result

	from operator import mul
	def main_diagonal_product_alt(mat):
    	return reduce(mul, (mat[i][i] for i in xrange(len(mat))))

if __name__ == '__main__'
	sol = Solution()