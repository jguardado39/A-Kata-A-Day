"""
Create a function that removes the first and last characters of a string.
You're given one parameter.

>>> remove_char('eloquent')
'loquen'
>>> remove_char('ok')
''
"""

def remove_char(s):
    return s[1:-1]
