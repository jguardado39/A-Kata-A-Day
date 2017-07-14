i# Modified: 07/13/17
# 
# Author: John Guardado (jguardado39)

"""
https://www.codewars.com/kata/578aa45ee9fd15ff4600090d

You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

"""

def sort_array(source_array):
  odds = iter(sorted(i for i in source_array if i  % 2))
  # print odds
  return [next(odds) if j % 2 else j for j in source_array]

# By PilgrimShadow
def sort_array_alt(arr):
  odds = sorted((x for x in arr if x%2 != 0), reverse=True)
  return [x if x%2==0 else odds.pop() for x in arr]