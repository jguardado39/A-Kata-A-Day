""" Given an array of intergers.
    Return an arry, where the first elements is the count of positive
    numbers and the second elements is sum of negative numbers.

    >>>count_positives_sum_negatives([1,2,3,-4,-5,-6])
    [3,-15]
"""
def count_positives_sum_negatives(arr):
    if arr == []:
        return []
    else:
        p,n = 0,0
        n = sum(int(y) for y in arr if y < 0)
        for x in arr:
            if x > 0:
                p += 1
            z = [p,n]
        return z
