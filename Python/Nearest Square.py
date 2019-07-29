def nearest_sq(n):
	"""
	Your task is to find the nearest square number, nearest_sq(n), of a positive integer n

	test.assert_equals(nearest_sq(1), 1)
	test.assert_equals(nearest_sq(2), 1)
	test.assert_equals(nearest_sq(10), 9)
	test.assert_equals(nearest_sq(111), 121)
	test.assert_equals(nearest_sq(9999), 10000)
	
	"""
	# range from 0 to n + 1
	for i in range (n + 1):
		if (i ** 2 == n):
			return n
		if (i ** 2 > n):
			# test to see what is the closest square
			if (abs(((i - 1) ** 2) - n) > abs((i ** 2) - n)):
				return i ** 2
			else:
				return (i - 1) ** 2




print(nearest_sq(1))
print(nearest_sq(2))
print(nearest_sq(10))
print(nearest_sq(111))
print(nearest_sq(9999))