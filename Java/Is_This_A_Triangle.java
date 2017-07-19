// Modified: 07/18/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/56606694ec01347ce800001b

Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

*/

class TriangleTester{
  public static boolean isTriangle(int a, int b, int c){
    if ((a+b) > c && (a+c) > b && (b+c) > a) {
      return true;
    }
    return false;
  }
}


// By Javatlacati
class TriangleTester{
  public static boolean isTriangle_alt(int a, int b, int c){
    return a + b > c && a + c > b && c + b > a;
  }
}