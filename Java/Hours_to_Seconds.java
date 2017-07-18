// Modified: 07/17/2017
//
// Author: jguardado39 (John Guardado)

/*

https://www.codewars.com/kata/596b041e224071ece200002e

The code provided is meant to return how many seconds there are in a given number of hours.

But it's not working properly.

Task

Fix the bug so we can all go home early.

Notes

The hours passed will be in the range 0 - 1000000

*/

public class Dinglemouse {

  // Return the number of seconds in a given number of hours
  public static long hoursToSeconds(final long hours) {
    final long ret = hours * 3600;
    return ret;
  }
}