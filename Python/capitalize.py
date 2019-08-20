def capitalize(s):
	"""
	Given a string, capitalize the letters that occupy even 
	indexes and odd indexes separately, and return as shown 
	below. Index 0 will be considered even.

	For example, capitalize("abcdef") = ['AbCdEf', 'aBcDeF']. 
	See test cases for more examples.

	The input will be a lowercase string with no spaces.

	Good luck!
	"""
	s = list(s)
	capitalizeEvenArray = []
	capitalizeOddArray = []
	finalArray = []

	for i in range(len(s)):
		if i % 2 == 0:
			capitalizeEvenArray.append(s[i].capitalize())
			capitalizeOddArray.append(s[i])
		else:
			capitalizeEvenArray.append(s[i])
			capitalizeOddArray.append(s[i].capitalize())

	finalArray.append(''.join(capitalizeEvenArray))
	finalArray.append(''.join(capitalizeOddArray))
	
	return finalArray

print(capitalize("abcdef"))       # ['AbCdEf', 'aBcDeF']
print(capitalize("codewars"))     # ['CoDeWaRs', 'cOdEwArS'])
print(capitalize("abracadabra"))  # ['AbRaCaDaBrA', 'aBrAcAdAbRa'])
print(capitalize("codewarriors")) # ['CoDeWaRrIoRs', 'cOdEwArRiOrS'])