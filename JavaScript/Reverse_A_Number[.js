// Modified: 08/10/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/555bfd6f9f9f52680f0000c5

Given a number, write a function to output its reverse digits. (e.g. given 123 the answer is 321)

Numbers should preserve their sign; i.e. a negative number should still be negative when reversed.

*/

function reverseNumber(n) {
  var m = Math.abs(n) + ""
  return (n > 0) ? parseInt(m.split('').reverse().join('')) : -1 * parseInt(m.split('').reverse().join(''));
}

// ZozoFouchtra
function reverseNumber(n) {
  return (n+'').match(/\d/g).reverse().join('') * (n<0? -1 : 1)
}