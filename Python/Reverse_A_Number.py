# Modified: 08/10/17
# 
# Author: John Guardado (jguardado39)

"""
https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5

Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

"""

def reverseNumber(n):
  m = [int(i) for i in str(abs(n))][::-1]
  return int(''.join(str(e) for e in m)) if n > 0  else -1 * int(''.join(str(e) for e in m))

def reverseNumber_alt(n):
    if n < 0: return -reverseNumber(-n)
    return int(str(n)[::-1])