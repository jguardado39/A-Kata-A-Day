// Modified: 07/13/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/55b42574ff091733d900002f

Make a program that filters a list of strings and returns a list with only your friends name in it.

If a name has exactly 4 letters in it, you can be sure that it has to be a friend of yours!

Ex: Input = ["Ryan", "Kieran", "Jason", "Yous"], Output = ["Ryan", "Yous"]
*/

function friend(friends){
  var friend = [];
  for (var i = 0; i < friends.length; i++) {
  	if (friends[i].length == 4) {
    	friend.push(friends[i]);
    }
  }
  return friend
}

// By NedDevine
function friend_alt(friends){
  return friends.filter(n => n.length === 4)
}