// Modified: 08/11/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/54ff3102c1bad923760001f3

Return the number (count) of vowels in the given string.

We will consider a, e, i, o, and u as vowels for this Kata.

*/

public class Vowels {

  public static int getCount(String str) {
    int vowelsCount = 0;
    for (int i = 0; i < str.length(); i++) {
      char ch = str.charAt(i);
      if (ch == 'a' || ch == 'e' || ch == 'i' || ch == 'o' || ch =='u') {
        vowelsCount++;
      }
    }
    return vowelsCount;
  }
}


// mortonfox
public class Vowels {
    public static int getCount_alt(String str) {
        return str.replaceAll("(?i)[^aeiou]", "").length();
    }
}