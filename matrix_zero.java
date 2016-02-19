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

        public static void null_row (int matrix[][], int row) {
                for (int i = 0; i < 4; i++) {
                        matrix[row][i] = 0;
                }
        }

        public static void null_column (int matrix[][], int column) {
                for (int i = 0; i < 4; i++) {
                        matrix[i][column] = 0;
                }
        }

        public static void main (String[] str) {
                int matrix[][] = {{1,2,0,4},{5,6,7,8},{9,10,11,12},{13,14,15,16}};
                boolean[] row = new boolean[matrix.length];
                boolean[] column = new boolean[matrix[0].length];

                print_matrix (matrix);
                for (int i = 0; i < matrix.length; i++) {
                        for (int j = 0; j < matrix.length; j++) {
                                if (matrix[i][j] == 0) {
                                        row[i] = true;
                                        column[j] = true;
                                }
                        }
                }

                for (int i = 0; i < row.length; i++) {
                        if (row[i]) {
                                null_row (matrix, i);
                        }
                }

                for (int j = 0; j < column.length; j++) {
                        if (column[j]) {
                                null_column (matrix, j);
                        }
                }
                print_matrix (matrix);

        }
}
