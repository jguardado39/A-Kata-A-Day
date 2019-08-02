def automorphic(n):
	"""
	Definition
	A number is called Automorphic number if 
	and only if its square ends in the same digits 
	as the number itself.

	Task
	Given a number determine if it Automorphic 
	or not .
	"""
	if (n == (n ** 2) % (10 ** len(str(n)))):
		return "Automorphic"
	return "Not!!"

print(automorphic(1))   # "Automorphic"
print(automorphic(3))   # "Not!!"
print(automorphic(6))   # "Automorphic"
print(automorphic(9))   # "Not!!"
print(automorphic(25))  # "Automorphic"
print(automorphic(53))  # "Not!!"
print(automorphic(76))  # "Automorphic"
print(automorphic(95))  # "Not!!"
print(automorphic(625)) # "Automorphic"
print(automorphic(225)) # "Not!!"