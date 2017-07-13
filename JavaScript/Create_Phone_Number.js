// Modified: 07/12/2017
//
// Author: jguardado39 (John Guardado)

/*



Write a function that accepts an array of 10 integers (between 0 and 9), that returns a string of those numbers in the form of a phone number.

Example:

createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) // => returns "(123) 456-7890"


The returned format must be correct in order to complete this challenge. 
Don't forget the space after the closing parenthese!

*/

function createPhoneNumber(numbers) {
  var numbers2 = ("" + numbers).replace(/\D/g, ''___);
  var m = numbers2.match(/^(\d{3})(\d{3})(\d{4})$/);
  return (!m) ? null : "(" + m[1] + ") " + m[2] + "-" + m[3];
}

// By madstorm
function createPhoneNumber_alt(numbers){
  var format = "(xxx) xxx-xxxx";
  
  for(var i = 0; i < numbers.length; i++)
  {
    format = format.replace('x', numbers[i]);
  }
  
  return format;
}