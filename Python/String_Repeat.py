"""
Write a function called repeatStr which repeats the given string string
exactly n times.

>>> repeat_str(4, 'a')
aaaa
>>> repeat_str(3, 'hello ')
'hello hello hello '
"""

def repeat_str(repeat, string):
    return ''.join([x for x in string]*repeat)
