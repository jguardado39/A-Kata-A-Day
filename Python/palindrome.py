def palindrome(num):
	"""
	A palindrome is a word, phrase, number, or
	other sequence of characters which reads the 
	same backward as forward. Examples of numerical 
	palindromes are:

	2332
	110011
	54322345

	For a given number num, write a function to test if 
	it's a numerical palindrome or not and return a boolean 
	(true if it is and false if not).

	Return "Not valid" if the input is not an integer or less
	than 0.
	"""
	if type(num) != int or num < 0:
		return "Not valid"

	temp = num
	reverse = 0
	while (temp > 0):
		digit = temp % 10
		reverse = reverse * 10 + digit
		temp = temp // 10
	if (num == reverse):
		return True
	return False


print(palindrome(1221))       # True
print(palindrome(123322))     # False
print(palindrome("ACCDDCCA")) # "Not valid"
print(palindrome("1221"))     # "Not valid"
print(palindrome(-450))       # "Not valid"