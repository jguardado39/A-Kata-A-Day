class Solution():
    '''
    Create a function with two arguments that will return a list of length N with multiples of X.

    Assume both the given number and the number of times to count will be positive numbers greater than 0.

    Return the results as an array (or list in Python, Haskell or Ellxir)

    # For example 

    count_by(1,10) #should return [1,2,3,4,5,6,7,8,9,10]
    count_by(2,5) #should return [2,4,6,8,10]
    '''
    def __init__(self):
        pass

    def count_by(x,n):
        count = 0
        y = 0
        z = []
        while count < n:
            y += x
            z.append(y)
            count += 1
        return z

if __name__ == '__main__':
    sol = Solution()
