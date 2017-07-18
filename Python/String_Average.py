i# Modified: 07/17/17
# 
# Author: John Guardado (jguardado39)

"""

https://www.codewars.com/kata/5966847f4025872c7d00015b

You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"

"""

def average_string(s):
    count, s  = 0, s.split(' ')
    name =  {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"}
    number = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    for i in s:
        if i not in number:
            return "n/a"
        count += number[i]
    return name[count // len(s)]

# By emptybox223
def average_string_alt(s):
    sn={"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    a=0
    try:
        for i in s.split():
            a+=sn[i]
        a/=len(s.split())
    except:
        return "n/a"
    return list(sn.keys())[list(sn.values()).index(int(a))]