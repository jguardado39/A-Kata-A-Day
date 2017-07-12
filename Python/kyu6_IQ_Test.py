class Solutioion():
    """
    https://www.codewars.com/kata/552c028c030765286c00007d

    Bob is preparing to pass IQ test. The most 
    frequent task in this test is to find out 
    which one of the given numbers differs 
    from the others. Bob observed that one 
    number usually differs from the others in 
    evenness. Help Bob — to check his answers, he 
    needs a program that among the given numbers 
    finds one that is different in evenness, and return 
    a position of this number.

    ! Keep in mind that your task is to help Bob 
    solve a real IQ test, which means indexes of 
    the elements start from 1 (not 0)

    Examples:
    
    iq_test("2 4 7 8 10") => 3 // Third number is odd, while the rest of the numbers are even

    iq_test("1 2 1 1") => 2 // Second number is even, while the rest of the numbers are odd

    """
    def __init__(self):
        pass

    def iq_test(numbers):
        numbers = [int(s) for s in numbers.split()]
        odd, even = [], []
        for i in numbers:
            if i % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        if len(odd) == 1:
            return numbers.index(odd[0]) + 1
        return numbers.index(even[0]) + 1

    def iq_test_alt(numbers):
          e = [int(i) % 2 == 0 for i in numbers.split()]

    return e.index(True) + 1 if e.count(True) == 1 else e.index(False) + 1
    
if __name__ == '__main__'
    sol = Solutioion()