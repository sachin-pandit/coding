import java.io.*;
import java.util.*;
import java.math.*;

public class average {
        static Hashtable<String, Integer> hash = new Hashtable<String, Integer>();
        static int parse_line (String str) {
                String[] parse = str.split(" ");
                String[] time = parse[4].split(":");
                int hour = 0;
                int minute = 0;
                int actual_time = 0;
                int temp = 0;
                int result = 0;
//System.out.println ("\nFlight : " + parse[1] + " Time : " + parse[4]);

                if (parse[5].equals("AM")) {
                        hour = Integer.parseInt (time[0]);
                        minute = Integer.parseInt (time[1]);
                        if (hour != 12)
                                actual_time = hour*60 + minute;
                        else
                                actual_time = minute;
                } else {
                        hour = Integer.parseInt (time[0]);
                        minute = Integer.parseInt (time[1]);
                        if (hour != 12)
                                actual_time = 12*60 + hour*60 + minute;
                        else
                                actual_time = 12*60 + minute;
                }

                if (hash.containsKey(parse[1])) {
                        temp = hash.get(parse[1]);
                        result = actual_time - temp;
                        hash.remove (parse[1]);
                } else {
                        hash.put (parse[1], actual_time);
//              System.out.println ("Putting " + parse[1] + " Time " + actual_time);
                        result = 0;
                }

  //              System.out.println ("Hour = " + hour + " Minute = " + minute + " actual_time = " + actual_time);
                return result;
        }

        static int getAvgGroundedTime(ArrayList<String> flightArray) {
                int total_time = 0;
                int temp = 0;
                int count = 0;
                for (int i = 0 ; i < flightArray.size(); i++) {
                        temp = parse_line (flightArray.get(i));
    //                    System.out.println ("Temp = " + temp);
                        if (temp != 0)
                                count++;
                        total_time += temp;
                }

                temp = (int)Math.ceil((float)total_time/(float)count);
      //          System.out.println ("Final value " + temp);
                return temp; // Return the average grounded time
        }

        public static void main (String[] str) {
                ArrayList<String> lines = new ArrayList<String>();
                lines.add("Flight #123 arrived at 11:23 AM");
                lines.add("Flight #2 arrived at 12:47 PM");
                lines.add("Flight #2 departed at 2:27 PM");
                lines.add("Flight #82 arrived at 03:03 PM");
                lines.add("Flight #82 departed at 05:12 PM");
                lines.add("Flight #123 departed at 11:59 PM");
                getAvgGroundedTime (lines);
        }
}

