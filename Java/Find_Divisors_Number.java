// Modified: 07/11/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/542c0f198e077084c0000c2e

Find the number of divisors of a positive integer n.

Example:

divisors 4  = 3 -- 1, 2, 4
divisors 5  = 2 -- 1, 5
divisors 12 = 6 -- 1, 2, 3, 4, 6, 12
divisors 30 = 8 -- 1, 2, 3, 5, 6, 10, 15, 30

*/

public class FindDivisor {

  public long numberOfDivisors(int n) {
		int count = 0;
    for (int i = 0; i < n; i++) {
    	if (n % (i+1) == 0) {
      	count ++;
      }
    }
   	return count;
  }
}