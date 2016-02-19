import java.util.*;

public class string {
        public static void main (String[] str) {
                //String str1 = "  MrSachinPandit  ";
                String str1 = str[0];
                char[] str1_arr = str1.toCharArray ();
                char[] result = new char[30];
                int space_count = 0;
                int length = 0;
                int i;

                for (i = 0; i < str1.length(); i++) {
                        if (str1_arr[i] == ' ') {
                                space_count++;
                        }
                }

                length = str1.length() + 2*space_count;

                for (i = str1.length() - 1; i >= 0; i--) {
                        if (str1_arr[i] != ' ') {
                                result[length - 1] = str1_arr[i];
                                length--;
                        } else {
                                result[length - 1] = '0';
                                result[length - 2] = '2';
                                result[length - 3] = '%';
                                length -= 3;
                        }
                }

                System.out.println ("Original = " + str1);
                System.out.println ("Result = " + String.valueOf (result));

        }
}
