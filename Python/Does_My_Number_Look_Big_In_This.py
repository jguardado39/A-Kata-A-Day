i# Modified: 07/18/17
# 
# Author: John Guardado (jguardado39)

"""


A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits.

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634

The Challenge:

Your code must return true or false depending upon whether the given number is a Narcissistic number.

Error checking for text strings or other invalid inputs is not required, only valid integers will be passed into the function.

"""

def narcissistic(value):
  digits = [int(i) for i in str(value)]
  total = 0
  
  for j in range(value):
    total += sum([k ** j for k in digits])
    if total == value:
      return True
    elif total < value:
      total = 0
    else:
      return False

# By javafreak
def narcissistic_alt(value):
    return value == sum(int(x) ** len(str(value)) for x in str(value))