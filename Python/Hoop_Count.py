"""
Write a program where Alex can input N how many times the hoop goes round
and it will return him an encouraging message.

>>> hoopCount(3)
"Keep at it until you get it"
>>> hoopCount(11)
"Great, now move on to trick "
"""

def hoopCount(n):
    if n < 10:
        return "Keep at it until you get it"
    return "Great, now move on to tricks"
