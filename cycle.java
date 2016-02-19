import java.util.*;


public class cycle {
 public static void main(String[] args) {

        int distance = 8;
        int[] radius = { 1, 3, 6, 2, 5 };
        int[] cost = { 5, 6, 8, 3, 4 };

        int[] ans = Circles(distance, radius, cost);

        for (int i = 0; i < ans.length; i++)
            System.out.print(ans[i] + " ");

        System.out.println();
    }

 statis int get_start_index ()

 static int[] Circles(int distance, int[] radius, int[] cost) {

        int j;
        int min_cost=-1, min_index=0;
        int key1, key2;
        int index=0;
        int k = 0;
        int[] result = new int[radius.length];
        int[] sorted_array = new int[radius.length];
        sorted_array = Arrays.sort (radius);
        for (int i = 0; i < radius.length; i++) {
            min_cost=-1;
            min_index = 0;
            for (j = 0; j < radius.length; j++){
                if(radius[i] + radius[j] >= distance) {
                    if((cost[i]+cost[j])<min_cost || min_cost==-1) {
                        min_cost = cost[i] + cost[j];
                        min_index = j;
                    }
                    if((cost[i]+cost[j])==min_cost) {
                        if(radius[j] > radius[min_index]) {
                            min_index=j;
                        }
                    }
                }
            }
            if (min_index == 0)
                result[k++] = 0;
            else
                result[k++] = min_index+1;
        }
        return result;
    }
}
