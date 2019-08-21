def is_palindrome(s):
	"""
	Write function isPalindrome that checks 
	if a given string (case insensitive) is 
	a palindrome.
	"""
    return s.lower() == s[::-1].lower()


print(is_palindrome('a'))      # True
print(is_palindrome('aba'))    # True
print(is_palindrome('Abba'))   # True
print(is_palindrome('malam'))  # True
print(is_palindrome('walter')) # False
print(is_palindrome('kodok'))  # True
print(is_palindrome('Kasue'))  # False