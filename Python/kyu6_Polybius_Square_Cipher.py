# Modified: 04/06/2017
#
# Author: jguardado39 (John Guardado)

class Solution():
	"""
	https://www.codewars.com/kata/542a823c909c97da4500055e

	Implement the Polybius square cipher.

	Replace every letter with a two digit number. 
	The first digit is the row number, and the 
	second digit is the column number of following 
	square. Letters 'I' and 'J' are both 24 in this 
	cipher:
	
		1	2	3	4	5
	1	A	B	C	D	E
	2	F	G	H	I/J	K
	3	L	M	N	O	P
	4	Q	R	S	T	U
	5	V	W	X	Y	Z

	Input will be valid (only spaces and uppercase 
	letters from A to Z), so no need to validate 
	them.

	Examples:

	polybius('A') # "11"
	polybius('POLYBIUS SQUARE CIPHER') # "3534315412244543 434145114215 132435231542"
	polybius('IJ') # "2424"
	polybius('CODEWARS') # "1334141552114243"

	"""
	def __init__(self):
		pass

	cipher = {
		'A': '11', 'B': '12', 'C': '13', 'D': '14', 'E': '15',
		'F': '21', 'G': '22', 'H': '23', 'I': '24', 'J': '24', 'K': '25',
		'L': '31', 'M': '32', 'N': '33', 'O': '34', 'P': '35',
		'Q': '41', 'R': '42', 'S': '43', 'T': '44', 'U': '45',
		'V': '51', 'W': '52', 'X': '53', 'Y': '54', 'Z': '55'
	}

	def polybius (text):
		return ''.join(cipher[s] if s in cipher else s for s in text)

	def polybius_alt(text):
    L = 'ABCDEFGHIKLMNOPQRSTUVWXYZJ'
    return ''.join(['24' if a == 'J' else str(L.index(a)/5 + 1) + str(L.index(a)%5 + 1) if a in L else a for a in text])
    
if __name__ == '__main__'
	sol = Solution()