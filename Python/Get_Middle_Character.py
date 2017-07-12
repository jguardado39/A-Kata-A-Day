"""
Given a word. Return the middle character of the word. If the word's
length is odd, return the middle charcter. If the word's lenght is even,
return the middle 2 charcters.
"""
def get_middle(s):
    if len(s) % 2 == 0:
        return s[len(s)/2 - 1:(len(s)/2) + 1]
    return s[len(s) // 2]
