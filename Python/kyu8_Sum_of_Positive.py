# Modififed: 04/11/2017
#
# Author: jguardado39 (John Guardado)

class Soluition():
	""" 
    https://www.codewars.com/kata/5715eaedb436cf5606000381

	You get an array of numbers, return the sum of all of the positives ones.

	Example [1,-4,7,12] => 1 + 7 + 12 = 20

    """
	def __init__(self):
		pass

	def positive_sum(arr):
	    return sum(int(x) for x in arr if x >= 0)

if __name__ == '__main__'
	sol = Solution()