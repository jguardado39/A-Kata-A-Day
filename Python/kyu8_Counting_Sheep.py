class Solution():
	'''
	Consider an array of sheep where some sheep maybe missing fromt their place. We need a function that counts the number of

	sheep present in the array(true means present).

	# For example

	[True,  True,  True,  False,
  True,  True,  True,  True ,
  True,  False, True,  False,
  True,  False, False, True ,
  True,  True,  True,  True ,
  False, False, True,  True]

  The correct answer would be 17.

  Hint: Don't forget to check for bad values like null/undefined
	'''
	def __init__(self):
		pass

	def count_sheeps(arrayOfSheeps):
	    count = 0
	    for x in arrayOfSheeps:
	        if x == True:
	            count += 1
	    return count

if __name__ == '__main__':
	sol = Solution()