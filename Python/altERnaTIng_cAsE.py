i# Modified: 07/13/17
# 
# Author: John Guardado (jguardado39)

"""
https://www.codewars.com/kata/56efc695740d30f963000557

Define to_alternating_case(char*) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

char source[] = "hello world";
char *upperCase = to_alternating_case(source);
(void)puts(upperCase); // outputs: HELLO WORLD

char source[] = "HELLO WORLD";
char *upperCase = to_alternating_case(source);
(void)puts(upperCase); // outputs: hello world

char source[] = "HeLLo WoRLD";
char *upperCase = to_alternating_case(source);
(void)puts(upperCase); // outputs: hEllO wOrld

"""

def to_alternating_case(string):
	return string.swapcase()

def to_alternating_case_alt(string):
    newString = ""
    for char in string:
    	if char.isupper() == True:
        	newString += char.lower()
        else:
        	newString += char.upper()
    return newString