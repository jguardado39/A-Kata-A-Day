"""
Write a funciton stringy that takes a size and returns a string of
alternating '1s' and '0s'.
The string should start with 1.

>>> stringy(6)
101010
"""

def stringy(size):
    c,t = 0, []
    while c <= size-1:
        if c % 2 == 0:
            t.append(1)
            c += 1
        else:
            t.append(0)
            c += 1
    return ''.join(str(e) for e in t)
