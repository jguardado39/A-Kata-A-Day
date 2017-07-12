"""
Your task is to convert strings to how they would be written by Jaden
Smith. The string are actual quotes from Jaden Smith, but they are not
capitalized in the same way he originally typed them.

>>> quote = "How can mirrors be real if our eyes aren't real"
>>> toJadenCase(quote)
""How Can Mirrors Be Real If Our Eyes Aren't Real""

"""
import re
def toJadenCase(string):
         return re.sub(r"[A-Za-z]+('[A-Za-z]+)?",
                   lambda mo: mo.group(0)[0].upper() +
                              mo.group(0)[1:].lower(),
                   string)
