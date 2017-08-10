// Modified: 07/20/2017
//
// Author: jguardado39 (John Guardado)

/*
Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer

*/

function squareDigits(num) {
  var final = 0;
  digit = num.toString(10).split('').map(function(t){return parseInt(Math.pow(t,2))});
 return parseInt(digit.join(''));
}

// By jeffsb
function squareDigits_alt(num){
  return Number(('' + num).split('').map(function (val) { return val * val;}).join('')); 
}