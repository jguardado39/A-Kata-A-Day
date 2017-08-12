// Modified: 08/11/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/546e2562b03326a88e000020

Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer

*/

public class SquareDigit {
  public int squareDigits(int n) {
    String s = n + "";
    String[] digits = s.split("");
    String output = "";
    for (String str : digits) {
      int i = Integer.parseInt(str);
      output += i * i;
    }
    return Integer.parseInt(output);
  }
}

public class SquareDigit {

  public int squareDigits_alt(int n) {
    String result = ""; 
    
    while (n != 0) {
      int digit = n % 10 ;
      result = digit*digit + result ;
      n /= 10 ;
    }
    
    return Integer.parseInt(result) ;
  }

}