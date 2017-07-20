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

Waiting for the Feedback! Thanks!


*/

function GetSum(a,b) {
  var sum = 0, ini = Math.min(a,b), fin = Math.max(a,b);
  //console.log(fin);
  for (var i = ini; i < fin + 1; i++) {
    // console.log(sum);
    sum += i;
  }
  return sum;
}

// By ryanwaits
const GetSum = (a, b) => {
  let min = Math.min(a, b),
      max = Math.max(a, b);
  return (max - min + 1) * (min + max) / 2;
}