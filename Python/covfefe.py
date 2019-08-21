def covfefe(s):
	"""
	Your are given a string. You must replace the 
	word(s) coverage by covfefe, however, if you don't 
	find the word coverage in the string, you must add 
	covfefe at the end of the string with a leading space.

	For the languages where the string is not immutable 
	(such as ruby), don't modify the given string, otherwise 
	this will break the test cases.
	"""
	if "coverage" in s:
		return s.replace("coverage", "covfefe")
	return s + " covfefe"

print(covfefe("coverage"))          # "covfefe"
print(covfefe("coverage coverage")) # "covfefe covfefe"
print(covfefe("nothing"))           # "nothing covfefe"
print(covfefe("double space "))     # "double space  covfefe"
print(covfefe("covfefe"))           # "covfefe covfefe"