// Modified: 08/09/2017
//
// Author: jguardado39 (John Guardado)

/*
https://www.codewars.com/kata/54da5a58ea159efa38000836

Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

*/

function findOdd(A) {
  var count = 0;
  for (var i = 0; i < A.length; i++) {
     count = count ^ A[i];
  }
  return count;
}

// cgb14d
function findOdd_alt(A) {
  return A.reduce(function(c,v){return c^v;},0);
}