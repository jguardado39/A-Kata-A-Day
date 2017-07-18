// Modified: 07/17/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/5966f6343c0702d1dc00004c

Create a function that will take any amount of money and break it down to the smallest number of bills as possible. Only integer amounts will be input, NO floats. This function should output an array, where each element in the array represents the amount of a certain bill type. The array will be set up in this manner:

array[0] ---> represents $1 bills

array[1] ---> represents $5 bills

array[2] ---> represents $10 bills

array[3] ---> represents $20 bills

array[4] ---> represents $50 bills

array[5] ---> represents $100 bills

In the case below, we broke up $365 into 1 $5 bill, 1 $10 bill, 1 $50 bill, and 3 $100 bills.

giveChange(365) // =>  [0,1,1,0,1,3]

In this next case, we broke $217 into 2 $1 bills, 1 $5 bill, 1 $10 bill, and 2 $100 bills.

giveChange(217) // => [2,1,1,0,0,2]

*/

function giveChange(amount) {
  hundred = Math.floor(amount / 100);
  amount -= 100 * hundred;
  fifty = Math.floor(amount/ 50);
  amount -= 50 * fifty;
  twenty = Math.floor(amount / 20);
  amount -= 20 * twenty;
  ten = Math.floor(amount / 10);
  amount -= 10 * ten;
  five = Math.floor(amount / 5);
  amount -= 5 * five;
  one = amount;  
  return [one, five, ten, twenty, fifty, hundred]
}

// By myjinxin2015
function giveChange(x) {
  for(var r=[1,5,10,20,50,100],i=5,t;i>=0;i--) 
    x>=r[i]? (t=r[i],r[i]=~~(x/r[i]),x-=r[i]*t) : r[i]=0
  return r
}