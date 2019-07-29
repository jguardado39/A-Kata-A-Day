def solution(string):
	"""
	Complete the solution so that it reverses 
	the string value passed into it.

	solution('world') # returns 'dlrow'

	Test.expect(solution('world') == 'dlrow')
	Test.expect(solution('hello') == 'olleh')
	Test.expect(solution('') == '')
	Test.expect(solution('h') == 'h')
	"""
	return string[::-1]

print(solution('world'))
print(solution('hello'))
print(solution(''))
print(solution('h'))