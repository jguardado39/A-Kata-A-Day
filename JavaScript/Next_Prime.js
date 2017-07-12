// Modified: 07/12/2017
//
// Author: jguardado39 (John Guardado)

/*
  
https://www.codewars.com/kata/58e230e5e24dde0996000070

I don't think we have this specific prime kata on codewars, yet.

It's really simple:

Get the next prime number!

You will get a number n (n>=0) and your task is to find the next prime number.

e.g: nextPrime(5)=>7 || nextPrime(12)=>13

Make sure to optimize your code. There will be huge numbers in the tests!

*/

function nextPrime(n) {
  return isPrime(n + 1);
}

function isPrime(m) {
  if (m <= 2) return 2;
  for (var i = 2; i < Math.sqrt(m) + 1; i++)
    if (m % i === 0) {
      return isPrime(m + 1);
    }
   return m;
}

// By smile67
function nextPrime_alt(n){
  n = n < 1 ? 1 : n;
  while (++n) {
     for (var f = 0, i = 2; i * i <= n; i++) if (n % i == 0) {f = 1; break}
     if (!f) return n
  }
}