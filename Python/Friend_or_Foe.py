# Modified: 07/13/17
# 
# Author: John Guardado (jguardado39)

"""


Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]

"""
def friend(x):
    friends = []
    for i in x:
        if len(i) == 4:
            friends.append(i)
    return friends

# By colbydauph
def friend_alt(x):
    return [f for f in x if len(f) == 4]