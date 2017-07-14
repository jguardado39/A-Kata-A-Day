// Modified: 07/13/2017
//
// Author: jguardado39 (John Guardado)

/*



You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sortArray([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]

*/

function sortArray(array) {
  var odd = array.filter(is_odd).sort(ascending);
  return array.map(replace_odd_inorder);
  
  function ascending(a, b) {
    return a > b;
  }
  
  function is_odd(num) {
    return num % 2;
  }
  
  function replace_odd_inorder(num) {
    return is_odd(num) ? odd.shift() : num;
  }
}

// By TraikL
function sortArray_alt(array) {
  const odd = array.filter((x) => x % 2).sort((a,b) => a - b);
  return array.map((x) => x % 2 ? odd.shift() : x);
}