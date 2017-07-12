"""
If we list all the natural numbers below 10 that are multiples of 3
or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
Find the solution so that it returns the sum of all the multiples of
3 or 5 below the number passes in.

>>> solution(10)
23

"""
def solution(number):
    tot, count = 0, 1
    while count < number:
        if count % 3 == 0 or count % 5 == 0:
            tot = tot + count
            count += 1
        elif count % 15 == 0:
            tot = tot + count
            count += 1
        else:
            count += 1
    return tot

""" Another solution """
#def solution(number):
#    return sum(x for x in range(number) if x % 3 == 0k or x % 5 == 0)
