# Modified: 04/06/2017
#
# Author: jguardado39 (John Guardado)

import string
import collections


class Solution():
	"""
	https://www.codewars.com/kata/565b9d6f8139573819000056/

	You have managed to incercept an importatnt
	message and you are trying to read it.

	You ralized  that the message has been encoded
	and can be decoded by switching each letter
	with a corresponding letter.

	You also notice that each letter is paired with
	the letter that coincides with when the
	alphabeth is reversed.

	For example: 'a' is encided with 'z', 'b' with 
	'y', 'c' with 'x', etc.

	You read the first sentence:

	"r slkv mlylwb wvxlwvh gsrh nvhhztv"

	After a few minutes you manage to decode it:

	"i hope nobody decodes this message"

	Create a funciton that will instaly decode any
	of these messages

	You can assume no punctuation or capitals,
	only lower case letters, but remember spaces!
	"""
	def __init__(self):
		pass

	def decode(message):
	    letters = collections.deque(string.ascii_lowercase)
	    letters.reverse()
	    letters = ''.join(list(letters))
	    return message.translate(string.maketrans(string.ascii_lowercase,letters))

	if __name__ ==  '__main__':
		sol = Solution()