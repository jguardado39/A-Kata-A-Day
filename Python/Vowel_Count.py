# Modified: 04/10/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	Return the number (count) of vowels in the given string.

	We will consider a, e, i, o, and u as vowels for this Kata.
	
	>>> getCount("abracadabra")
	>>> 5
	
	"""

	def __init__(self):
		pass

	def getCount(inputStr):
	    num_vowels = 0
	    for char in inputStr:
	        if char  in "aeiouAEIOU":
	            num_vowels += 1
	    return num_vowels

    def getCount_alt(inputStr):
    	return sum(1 for let in inputStr if let in "aeiouAEIOU")

if __name__ == '__main__':
	sol = Solution()
