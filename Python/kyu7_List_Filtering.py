# Modified: 04/12/2017
#
# Author: jguardado39 (John Guardado)

class Solution(object):
	"""
	https://www.codewars.com/kata/53dbd5315a3c69eed20002dd
	
	In this kata you will create a function that takes a 
	list of non-negative integers and strings and 
	returns a new list with the strings filtered out.

	Example

	filter_list([1,2,'a','b']) == [1,2]

	filter_list([1,'a','b',0,15]) == [1,0,15]

	filter_list([1,2,'aasf','1','123',123]) == [1,2,123]

	"""
	def __init__(self, arg):
		super(Solution, self).__init__()
		self.arg = arg
	
	def filter_list(l):
		m = []
		for i in l:
			if isinstance(i, int):
				m.append(i)
		return m

	def filter_list_alt(l):
		'return a new list with the strings filtered out'
		return [i for i in l if not isinstance(i, str)]

if __name__ == '__main__':
    sol = Solution()	