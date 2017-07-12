"""
Given the number N, populate an array with all numbers up to and
including that number, but excluding zero.

>>> monkey_count(10)
[1,2,3,4,5,6,7,8,9,10]
"""

def  monkey_count(n):
    return list(range(1, n + 1))
