def count_sheep(n):
	"""
	If you can't sleep, just count sheep!!

	Task:
	Given a non-negative integer, 3 for example, return a string with 
	a murmur: "1 sheep...2 sheep...3 sheep...". Input will always be 
	valid, i.e. no negative integers.
	"""	
	return ''.join([str(x) + ' sheep...' for x in range(1, n + 1)])

print((count_sheep(1), "1 sheep..."))                     # "1 sheep..."
print((count_sheep(2), "1 sheep...2 sheep..."))           # "1 sheep...2 sheep..."
print((count_sheep(3), "1 sheep...2 sheep...3 sheep...")) # "1 sheep...2 sheep...3 sheep..."