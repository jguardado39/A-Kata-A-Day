i# Modified: 07/18/17
# 
# Author: John Guardado (jguardado39)

"""

https://www.codewars.com/kata/56d0a591c6c8b466ca00118b

Triangular number is the amount of points that can fill equilateral triangle.

Example: the number 6 is a triangular number because all sides of a triangle has the same amount of points.

Hint!
T(n) = n * (n + 1) / 2,
n - is the size of one side.
T(n) - is the triangular number.

Given a number 'T' from interval [1; 2147483646], find if it is triangular number or not.

Appreciate the feedback!

"""

def is_triangular(t):
    t = int(t)
    for i in range(t + 1):
      if (i * (i + 1) / 2) == t:
          return True
    return False

# By TheBMachine
def is_triangular(t):
    return (8 * t + 1)**.5 % 1 == 0