// Modified: 07/17/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/5966847f4025872c7d00015b

You are given a string of numbers between 0-9. Find the average of these numbers and return it as a floored whole number (ie: no decimal places) written out as a string. Eg:

"zero nine five two" -> "four"

If the string is empty or includes a number greater than 9, return "n/a"

*/

function averageString(str) {
  var number = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9};
  var  name =  {0 : "zero", 1 : "one", 2 : "two", 3 : "three", 4 : "four", 5 : "five", 6 : "six", 7 : "seven", 8 : "eight", 9 : "nine"};
  var count = 0;
  var split = str.split(' ');
  for (var i = 0; i < split.length; i++) {
    if (!(split[i] in number)) {
      return "n/a"
    }
    count += number[split[i]];
  }
  return name[parseInt(count / split.length)]
}

// By SandQueen
function averageString_alt(str) {
  let obj = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  return obj[Math.floor(str.split(' ').map(x=>obj.includes(x)?obj.indexOf(x):NaN).reduce((a, b)=>a+b)/str.split(' ').length)]||'n/a'
}