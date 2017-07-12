#Welcome. In this kata, you are asked to square every digit of a number.
#For example, if we run 9119 through the function, 811181 will come out.
#Note: The function accepts an integer and returns an integer

def square_digit(nim):
    """
    test.assert_equals(square_digit(9119),811181)
    
    """
    n = [int(x) ** 2 for x in str(nim)]
    m = int(str(''.join([str(y) for y in n])))
    return m
