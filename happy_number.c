#include <stdio.h>
#include <stdlib.h>

int
find_sum (int num) {
        int new_num = 0;
        int rem = 0;
        while (num > 0) {
                rem = num % 10;
                new_num += rem * rem;
                num = num/10;
        }
        return new_num;
}

int
check_if_present (int *arr, int count, int new_num) {
        int i;
        /*
        for (i = 0; i <= count; i++)
                printf ("%d ", arr[i]);
        */
        //printf ("\n");
        for (i = 0; i <= count; i++) {
                if (arr[i] == new_num)
                        return 1;
        }
        return 0;
}

int
find_if_happy (int num, int *happy) {
        int new_num;
        int count = 0;
        int first = 0;
        int arr[100];
        int i = 0;
        int ret = 0;

        for (i = 0 ; i < 100; i++)
                arr[i] = 0;

        arr[count] = num;
        count++;
        new_num = num;
        while (new_num != 1) {
                new_num = find_sum (new_num);
                //printf ("New Num = %d\n", new_num);
                if (check_if_present (arr, count, new_num)) {
                        *happy = 0;
                        return count;
                }
                arr[count] = new_num;
                count++;
        }
        *happy = 1;
        return count;
}

int main () {
        int i = 0;
        int arr[10];
        int ret = 0;
        int happy = 0;


        while (i < 10) {
                scanf ("%d", &arr[i]);
                i++;
        }

        i = 0;
        while (i < 10) {
                ret = 0;
                happy = 0;
                if (arr[i] == 1) {
                        printf ("happy 0\n");
                } else {
                        ret = find_if_happy (arr[i], &happy);
                        if (happy ==0) {
                                printf ("unhappy %d\n", ret);
                        } else {
                                printf ("happy %d\n", ret - 1);
                        }
                }
                i++;
        }
        return 1;
}
