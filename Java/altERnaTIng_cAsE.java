// Modified: 07/14/2017
//
// Author: jguardado39 (John Guardado)

/*



Define to_alternating_case(char*) such that each lowercase letter becomes uppercase and each uppercase letter becomes lowercase. For example:

char source[] = "hello world";
char *upperCase = to_alternating_case(source);
(void)puts(upperCase); // outputs: HELLO WORLD

char source[] = "HELLO WORLD";
char *upperCase = to_alternating_case(source);
(void)puts(upperCase); // outputs: hello world

char source[] = "HeLLo WoRLD";
char *upperCase = to_alternating_case(source);
(void)puts(upperCase); // outputs: hEllO wOrld

*/

public class StringUtils {
  
  public static String toAlternativeString(String string) {
    char [] chars = string.toCharArray();
    for (int i = 0; i < chars.length; i++) {
      char c = chars[i];
      if (Character.isUpperCase(c)) {
        chars[i] = Character.toLowerCase(c);
      } else if (Character.isLowerCase(c)) {
        chars[i] = Character.toUpperCase(c);
      }
    }
    return new String(chars);
  }
}