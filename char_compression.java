import java.util.*;

public class char_compression {
        public static void main (String[] str) {
                String str1 = str[0];
                char[] str1_arr = str1.toCharArray();
                int i;
                StringBuffer result = new StringBuffer ("");
                int result_index = 0;
                int count = 0;
                Character ch;

                for (i = 0; i < str1.length(); i++) {
                        ch = str1_arr[i];
                        count = 0;
                        while (i < str1.length() && str1_arr[i] == ch) {
                                count++;
                                i++;
                        }
                        i--;
                        result.append(ch);
                        result.append(count);
                }

                if (result.length() == 2 * str1.length())
                        System.out.println ("Result = " + str1);
                else
                        System.out.println ("Result = " + result);

        }
}
