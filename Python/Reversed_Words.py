i# Modified: 07/15/17
# 
# Author: John Guardado (jguardado39)

"""

Complete the solution so that it reverses all of the words within the string passed in.

Example:

reverseWords("The greatest victory is that which requires no battle")
// should return "battle no requires which that is victory greatest The"

"""

def reverseWords(str):
  str1 = str.split()
  str1.reverse()
  return ' '.join(str1)


# By jhoffner
def reverseWords(str):
    return " ".join(str.split(" ")[::-1])