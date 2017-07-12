import string
import collections

def encryptor(key, message):
	# encrypt = ''
	# for i in message:
	# 	if i.isalpha():
	# 		stayInAlphabet = ord(i) + key
	# 		if stayInAlphabet > ord('z'):
	# 			stayInAlphabet -= 26
	# 		finalLetter = chr(stayInAlphabet)
	# 		encrypt += finalLetter
	# return encrypt
	upper = collections.deque(string.ascii_uppercase)
	lower = collections.deque(string.ascii_lowercase)

	upper.rotate(key)
	lower.rotate(key)

	upper = ''.join(list(upper))
	lower = ''.join(list(lower))

	return message.translate(string.maketrans(string.ascii_uppercase,upper)).translate(string.maketrans(string.ascii_lowercase, lower))