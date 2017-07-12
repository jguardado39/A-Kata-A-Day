class Solution():
	"""
	https://www.codewars.com/kata/576757b1df89ecf5bd00073b

	Build Tower by given number of floor (intergers and always greater than 0).

	Tower block is represented as '*'

	# for example, a tower of 3 floors looks like below
	[
      ['  *  '],
      [' *** '],
      ['*****']
    ]
    """
    def __init__(self):
    	pass

	def tower_builder(n_floors):
		floors = []
		n = n_floors
		for i in range(n_floors):
			n -= 1
			floors.append(' ' * n + '*' * (i * 2 + 1) + ' ' * n)
		return floors

if __name__ == '__main__':
	sol = Solution()

	print(repr(sol.tower_builder(6)))