import java.util.*;

public class string_rotate {
        public static void main (String[] str) {
                String str1 = str[0];
                String str2 = str[1];
                StringBuffer result = new StringBuffer ("");

                result.append (str1);
                result.append (str1);

                //System.out.println ("result = " + result);
                if (result.toString().toLowerCase().contains(str2.toString().toLowerCase())) {
                        System.out.println ("Yes it is!!");
                } else {
                        System.out.println ("Sorry it is not..");
                }

        }
}
