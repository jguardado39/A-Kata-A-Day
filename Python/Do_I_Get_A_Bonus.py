# Modified: 07/11/2017
#
# Author: jguardado39 (John Guardado)

"""
https://www.codewars.com/kata/56f6ad906b88de513f000d96

It's bonus time in the big city! The fatcats are rubbing their paws in anticipation... but who is going to make the most money?

Build a function that takes in two arguments (salary, bonus). Salary will be an integer, and bonus a boolean.

If bonus is true, the salary should be multiplied by 10. If bonus is false, the fatcat did not make enough money and must receive only his stated salary.

Return the total figure the individual will receive as a string prefixed with '£' (JS and Java) or '$' (C#, C++, Ruby, Clojure, Elixir, PHP and Python).

"""

def bonus_time(salary, bonus):
    if bonus == 1:
        return "$"+ str(salary * 10)
    else:
        return "$" + str(salary)