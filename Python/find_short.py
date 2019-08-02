def find_short(s):
	"""
	Simple, given a string of words, return the length 
	of the shortest word(s).

	String will never be empty and you do not need 
	to account for different data types.
	"""
	text_array = s.split()
	shortest_word = len(text_array[0])
	for i in range(1,len(text_array)):
		if len(text_array[i]) < shortest_word:
			shortest_word = len(text_array[i])
	return shortest_word


print(find_short("bitcoin take over the world maybe who knows perhaps"))                # 3
print(find_short("turns out random test cases are easier than writing out basic ones")) # 3
print(find_short("lets talk about javascript the best language"))                       # 3
print(find_short("i want to travel the world writing code one day"))                    # 1
print(find_short("Lets all go on holiday somewhere very cold"))                         # 2