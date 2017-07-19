// Modified: 07/18/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/56606694ec01347ce800001b

Implement a method that accepts 3 integer values a, b, c. The method should return true if a triangle can be built with the sides of given length and false in any other case.

(In this case, all triangles must have surface greater than 0 to be accepted).

*/

function isTriangle(a,b,c) {
  longSide = Math.max(a,b,c);
  shortSide = Math.min(a+b, a+c, b+c);
  if (shortSide > longSide) {
    return true;
  }
  return false;
}

// By CrazyMerlyn
function isTriangle_alt(a,b,c)
{
  [a, b, c] = [a, b, c].sort((x, y) => x-y);
  
  return a+b > c;
}