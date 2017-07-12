# Modified: 07/12/2017
#
# Author: jguardado39 (John Guardado)


"""
https://www.codewars.com/kata/58e230e5e24dde0996000070

I don't think we have this specific prime kata on codewars, yet.

It's really simple:

Get the next prime number!

You will get a number n (n>=0) and your task is to find the next prime number.

e.g: nextPrime(5)=>7 || nextPrime(12)=>13

Make sure to optimize your code. There will be huge numbers in the tests!

"""

def nextPrime(n):
  return is_prime(n+1)
  
def is_prime(m):
  if m < 2: return 2
  for i in range(2, int(m ** 0.5) + 1):
    if m % i == 0:
      m += 1
      return is_prime(m)
  return m

def nextPrime_alt(n):
    if n <= 2: return 2 + (n == 2)
    p, d = n + [1, 4, 3, 2, 1, 2][n % 6], 4 - 2 * (0 < n % 6 < 5)
    while True:
        for k in range(5, int(p ** .5) + 1, 6):
            if not p % k or not p % (k + 2): break
        else: return p
        p, d = p + d, 6 - d