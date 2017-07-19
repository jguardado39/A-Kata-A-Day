// Modified: 07/18/2017
//
// Author: jguardado39 (John Guardado)

/*

Description:

Groups of characters decided to make a battle. Help them to figure out which group is more powerful. Create a function that will accept 2 variables and return the one who's stronger.

Rules:

Each character have its own power: A = 1, B = 2, ... Y = 25, Z = 26
Only capital chatacters can and will participate a battle.
Only two groups to a fight.
Group whose total power (A + B + C + ...) is bigger wins.
If the powers are equal, it's a tie.

Examples:

battle("ONE", "TWO"); // => "TWO"`
battle("ONE", "NEO"); // => "Tie!"

*/

function battle(x, y) {
  var alphabeth = {"A":1, "B":2, "C":3, "D":4, "E":5, "F":6, "G":7, "H":8, "I": 9, "J": 10, "K":11, "L":12, "M":13, "N":14, "O":15, "P":16, "Q":17, "R":18, "S":19, "T": 20, "U":21, "V":22, "W":23, "X":24, "Y":25, "Z":26}  
  xSplit = x.split("");
  var sum1 = 0, sum2 = 0
  for (var i = 0; i < xSplit.length; i++) {
    sum1 += alphabeth[xSplit[i]];
  }
  ySplit = y.split("");
  for (var j = 0; j < ySplit.length; j++) {
    sum2 += alphabeth[ySplit[j]];
  }  
  if (sum1 === sum2) {
    return "Tie!";
  } else if (sum1 > sum2) {
    return x;
  } else {
    return y;
  }
}

// By adrian.eye
function battle_alt(x, y) {
  a = x.split("").map(z => z.charCodeAt(0)-64).reduce((a,b) => a+b, 0)
  b = y.split("").map(z => z.charCodeAt(0)-64).reduce((a,b) => a+b, 0)
  return a < b ? y : a > b ? x : "Tie!"
}