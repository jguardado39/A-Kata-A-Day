i# Modified: 07/18/17
# 
# Author: John Guardado (jguardado39)

"""
https://www.codewars.com/kata/5418a1dd6d8216e18a0012b2

In this Kata, you will implement The Luhn Algorithm, which is used to help validate credit card numbers.

Given a positive integer of up to 16 digits, return true if it is a valid credit card number, and false if it is not.

Here is the algorithm:

If there are an even number of digits, double every other digit starting with the first, and if there are an odd number of digits, double every other digit starting with the second. Another way to think about it is, from the right to left, double every other digit starting with the second to last digit.

1714 => [1*, 7, 1*, 4] => [2, 7, 2, 4]

12345 => [1, 2*, 3, 4*, 5] => [1, 4, 3, 8, 5]

891 => [8, 9*, 1] => [8, 18, 1]

If a resulting doubled number is greater than 9, replace it with either the sum of it's own digits, or 9 subtracted from it.

[8, 18*, 1] => [8, (1+8), 1] => [8, 9, 1]

(or)

[8, 18*, 1] => [8, (18-9), 1] => [8, 9, 1]

Sum all of the final digits

[8, 9, 1] => 8+9+1 => 18

Finally, take that sum and divide it by 10. If the remainder equals zero, the original credit card number is valid.

18 (modulus) 10 => 8.  

8 does not equal 0, so 891 is not a valid credit card number.

"""

def validate(n):
    digits = list(int(i) for i in str(n))
    odd_index = digits[-1::-2]
    sum1 = sum(odd_index)
    even_index = [i*2 for i in digits[-2::-2]]
    for j in even_index:
        if j > 9:
            sum1 += j // 10 + j % 10
        else:
            sum1 += j
    if sum1 % 10 == 0:
        return True
    return False


# By cdw9
def validate_alt(n):
    digits = [int(x) for x in str(n)]
    for x in xrange(len(digits)-2, -1, -2):
        digits[x] = sum(map(int, str(digits[x] * 2)))
    return sum(digits) % 10 == 0