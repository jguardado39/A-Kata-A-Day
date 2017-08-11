// Modified: 08/10/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/54ff3102c1bad923760001f3

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.\

*/

function getCount(str) {
  var m = str.match(/[aeiou]/gi);
  return m === null ? 0 : m.length;
}

// By Balkoth
function getCount_alt(str) {
  return (str.match(/[aeiou]/ig)||[]).length;
}