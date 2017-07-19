// Modified: 07/18/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/5287e858c6b5a9678200083c

A Narcissistic Number is a number which is the sum of its own digits, each raised to the power of the number of digits.

For example, take 153 (3 digits):

    1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

and 1634 (4 digits):

    1^4 + 6^4 + 3^4 + 4^4 = 1 + 1296 + 81 + 256 = 1634

The Challenge:

Your code must return true or false depending upon whether the given number is a Narcissistic number.

Error checking for text strings or other invalid inputs is not required, only valid integers will be passed into the function.

*/

function narcissistic(value) {
  var valStr = '' + value;
  var valLength = valStr.length;
  console.log(valLength);
  var result = 0;  
  for (var i in valStr) {
    result += Math.pow((+valStr[i]), valLength);
  }
    return result === value;
}

// By colbydauph
function narcissistic_alt( value ) {
  return ('' + value).split('').reduce(function(p, c){
    return p + Math.pow(c, ('' + value).length)
    }, 0) == value;
}
