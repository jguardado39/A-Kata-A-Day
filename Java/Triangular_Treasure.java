// Modified: 07/12/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/525e5a1cb735154b320002c8

Triangular numbers are so called because of the equilateral triangular shape that they occupy when laid out as dots. i.e.

1st (1)   2nd (3)    3rd (6)
*          **        ***
           *         **
                     *

You need to return the nth triangular number. You should return 0 for out of range values:

all [
  triangular 0     == 0,
  triangular 2     == 3,
  triangular 3     == 6,
  triangular (-10) == 0
] -- True

*/

public class Triangular {
    public static int triangular(int n) {
    	if (n < 0) {
      	return 0;
      }
    return n * (n + 1) / 2;
    }
}

// By JulianNicholls
public class Triangular_alt {
    public static int triangular(int n) {
        return (n <= 0) ? 0 : n * (n + 1) / 2;
    }
}