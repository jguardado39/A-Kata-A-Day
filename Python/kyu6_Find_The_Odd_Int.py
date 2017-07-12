class Solutions():
	"""
	Given an array, find the int that appears an odd number of times.

	There will always be only one integer that appears an odd number of times.

	# for example 

	DNA_strand ("ATTGC") # return "TAACG"

	DNA_strand ("GTAT") # return "CATA"
	"""
	def __init__(self):
		pass

	def find_it(seq):
	    cnt = 0
	    for i in seq:
	        cnt = cnt ^ i  #Bitwise XOR
	    return cnt

if __name__ == '__main__':
	sol = Solution()