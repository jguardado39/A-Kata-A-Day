def expression_matter(a, b, c):
"""
Given three integers a ,b ,c, return the largest number obtained after inserting the following operators and brackets: +, *, ().

expressionsMatter(1,2,3)  ==>  return 9
expressionsMatter(1,1,1)  ==>  return 3
expressionsMatter(9,1,1)  ==>  return 18
"""
    expressionOne = a * (b + c)
    expressionTwo = a * b * c
    expressionThree = a + b * c
    expressionFour = (a + b) * c
    expressionFive = a + b + c
    return max(expressionOne, expressionTwo, expressionThree, expressionFour, expressionFives)
