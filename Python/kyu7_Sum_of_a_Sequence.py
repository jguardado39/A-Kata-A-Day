# Modififed: 04/11/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	https://www.codewars.com/kata/586f6741c66d18c22800010a	
	
	Your task is to make function, which returns 
	the sum of a sequence of integers.

	The sequence is defined by 3 non-negative 
	values: begin, end, step.

	If begin value is greater than the end, function 
	should returns 0

	Examples:

	sequenceSum(2,2,2) === 2
	sequenceSum(2,6,2) === 12 // 2 + 4 + 6
	sequenceSum(1,5,1) === 15 // 1 + 2 + 3 + 4 + 5
	sequenceSum(1,5,3) === 5 // 1 + 4

	"""
	def __init__(self):
		pass

	def sequence_sum(begin_number, end_number, step):
	    sum = 0
	    while begin_number <= end_number:
	        sum += begin_number
	        begin_number += step
	    return sum

    def sequence_sum_alt(begin_number, end_number, step):
    	return sum(range(start, end + 1, step))

if __name__ == '__main__'
	sol = Solution()