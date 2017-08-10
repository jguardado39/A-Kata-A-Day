// Modified: 08/10/2017
//
// Author: jguardado39 (John Guardado)

/*



Given an array, find the int that appears an odd number of times.

There will always be only one integer that appears an odd number of times.

*/

public class FindOdd {
	public static int findIt(int[] A) {
    int i;
    int res = 0;
    for (i = 0; i < A.length; i++) {
      res = res ^ A[i];
    }
    return res;
  }
}