// Modified: 07/19/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/5526fc09a1bbd946250002dc

You are given an array (which will have a length of at least 3, but could be very large) containing integers. The array is either entirely comprised of odd integers or entirely comprised of even integers except for a single integer N. Write a method that takes the array as an argument and returns N.

For example:

[2, 4, 0, 100, 4, 11, 2602, 36]

Should return: 11

[160, 3, 1719, 19, 11, 13, -21]

Should return: 160

*/

function findOutlier(integers){
  var odd_int = [], even_int = [];
  for (var i = 0; i < integers.length; i++) {
    if (integers[i] % 2 === 0) {
      even_int.push(integers[i])
    } else {
      odd_int.push(integers[i])
    }
  }
  if (odd_int.length === 1) {
    return odd_int[0];
  }
  return even_int[0];
}

// By obolensky
function findOutlier(int){
  var even = int.filter(a=>a%2==0);
  var odd = int.filter(a=>a%2!==0);
  return even.length==1? even[0] : odd[0];
}