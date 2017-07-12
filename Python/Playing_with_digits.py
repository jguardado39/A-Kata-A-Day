"""
Some numbers have funny properties

89 --> 8^1 + 9^1 = 89 * 1
659 --> 6^2 + 9^3 + 5^4 = 659 * 2
46288 --> 4 ^3 + 6^4 + 2^5 + 8^6 + 8^7 = 2360688 = 46288 * 51

Given a positive integer N written as ABCD....(where a,b,c,d,... be
unique digits) and a positive integer P. We want to find a positive
K, if it exists, such as the sum of the digits of N taken to the
successive powers of P is equal to K * N.

If it is the case we will return K, if not return -1.

>>> dig_pow(89,1)
1
>>> dig_pow(92,1)
-1
"""

def dig_pow(n,p):
    def total_count(c,d):
        tot, lst = 0, [int(i) for i in str(c)]
        while len(lst) != 0:
            tot = tot + lst[0] ** d
            d += 1
            lst.pop(0)
        return tot
    def divisible_by(a,b):
        prod = a // b
        if  a == b * prod:
            return prod
        return -1
    return divisible_by(total_count(n,p),n)
