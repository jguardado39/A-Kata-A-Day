// Modified: 07/12/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/5412509bd436bd33920011bc

Usually when you buy something, you're asked whether your credit card number, phone number or answer to your most secret question is still correct. However, since someone could look over your shoulder, you don't want that shown on your screen. Instead, we mask it.

Your task is to write a function maskify, which changes all but the last four characters into '#'.

Examples

maskify("4556364607935616") == "############5616"
maskify(     "64607935616") ==      "#######5616"
maskify(               "1") ==                "1"
maskify(                "") ==                 ""

// "What was the name of your first pet?"
maskify("Skippy")                                   == "##ippy"
maskify("Nananananananananananananananana Batman!") == "####################################man!"


*/

function maskify(cc) {
  if (cc.length < 5) {
    return cc
  }
  return '#'.repeat(cc.length - 4) + cc.substr(cc.length - 4)
}

// by laoris
function maskify_alt(cc) {
  return cc.slice(0, -4).replace(/./g, '#') + cc.slice(-4);
}