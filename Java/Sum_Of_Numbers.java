// Modified: 07/19/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/55f2b110f61eb01779000053

Given two integers, which can be positive and negative, find the sum of all the numbers between including them too and return it. If both numbers are equal return a or b.

Note! a and b are not ordered!

Example: 
GetSum(1, 0) == 1   // 1 + 0 = 1
GetSum(1, 2) == 3   // 1 + 2 = 3
GetSum(0, 1) == 1   // 0 + 1 = 1
GetSum(1, 1) == 1   // 1 Since both are same
GetSum(-1, 0) == -1 // -1 + 0 = -1
GetSum(-1, 2) == 2  // -1 + 0 + 1 + 2 = 2

*/

public class Sum
{
   public int GetSum(int a, int b) {
     int sum = 0;
     int max = Math.max(a,b);
     int min= Math.min(a,b);
     for (int i = min; i < max + 1; i++) {
       sum += i;
     }
     return sum;
   }
}

// By Unnamed
public class Sum
{
  public int GetSum_alt(int a, int b)
  {
    return (a + b) * (Math.abs(a - b) + 1) / 2;
  }
}