# Modified: 04/06/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	https://www.codewars.com/kata/58373ba351e3b615de0001c3

	The Mormons are trying to find new followers 
	and in order to do that they embark on 
	missions.

	Each time they go on a mission, every Mormons 
	converts a fixed number of people (reach) into 
	followers. This continues and every freshly 
	converted Mormon as well as every original 
	Mormon go on another mission and convert 
	the same fixed number of people each. The 
	process continues until they reach a predefined 
	target number of followers (input into the 
	model).

	Converted Mormons are unique so that there's 
	no duplication amongst them.

	Create a function Mormons(startingNumber, 
	reach, target) that calculates how many 
	missions Mormons need to embark on, in order 
	to reach their target. While each correct 
	solution will pass, for more fun try to make a 
	recursive function.

	All model inputs are valid positive integers.

	"""
	def __init__(self):
		pass

	def mormons(starting_number, reach, target):
		if starting_number >= target:
			return 0
		return 1 + mormons(starting_number + (reach * starting_number), reach, target)

	def mormons_alt(starting_number, reach, count = 0):
	if starting_number >= target:
        return count
    else:
        return mormons(starting_number * reach + starting_number, reach, target, count + 1)

if __name__ == '__main__':
	sol = Solution()