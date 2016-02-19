import java.util.*;

public class rotate_matrix {
        public static void main(String[] str) {
                int[][] matrix = {{1,2,3,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
                int i,j, layer;
                for (i = 0; i < 4; i++) {
                        for (j = 0; j < 4; j++) {
                                System.out.print (" " + matrix[i][j] + " ");
                        }
                        System.out.println("");
                }

                for (layer = 0; layer < 2; layer++) {
                        int first = layer;
                        int last = 4 - 1 - layer;
                        for (i = first; i < last; i++) {
                                int offset = i - first;
                                int top = matrix[first][i];

                                matrix[first][i] = matrix[last-offset][first];
                                matrix[last-offset][first] = matrix[last][last-offset];
                                matrix[last][last-offset] = matrix[i][last];
                                matrix[i][last] = top;

                        }
                }

                System.out.println("");
                for (i = 0; i < 4; i++) {
                        for (j = 0; j < 4; j++) {
                                System.out.print (" " + matrix[i][j] + " ");
                        }
                        System.out.println("");
                }

        }
}
