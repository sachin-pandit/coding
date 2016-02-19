import java.util.*;

public class matrix_zero {
        public static void print_matrix (int matrix[][]) {
                for (int i = 0; i < 4; i++) {
                        for (int j = 0; j < 4; j++) {
                                System.out.print (" " + matrix[i][j] + " ");
                        }
                        System.out.println ("");
                }
        }

        public static void fill_zero (int matrix[][], int row, int column) {
                for (int i = 0; i < 4; i++) {
                        matrix[row][i] = 0;
                        matrix[i][column] = 0;
                }
        }

        public static void main (String[] str) {
                int matrix[][] = {{1,2,0,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
                int final_matrix[][] = new int[4][4];
                System.out.println ("Before:");
                for (int i = 0; i < 4; i++) {
                        for (int j = 0; j < 4; j++) {
                                final_matrix[i][j] = matrix[i][j];
                        }
                }
                print_matrix (matrix);
                for (int i = 0; i < 4; i++) {
                        for (int j = 0; j < 4; j++) {
                                if (matrix[i][j] == 0) {
                                        fill_zero (final_matrix, i, j);
                                }
                        }
                }
                System.out.println ("After:");
                print_matrix (final_matrix);

        }
}
