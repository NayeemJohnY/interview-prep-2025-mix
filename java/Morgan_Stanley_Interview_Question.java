
import java.util.Arrays;

public class Morgan_Stanley_Interview_Question {

    // Helper method to reverse a subarray in place
    public static void reverse(int[] arr, int left, int right) {
        while (left < right) {
            int temp = arr[left];
            arr[left++] = arr[right];
            arr[right--] = temp;
        }
    }

    public static void main(String[] args) {
        int[] arr = {7, 6, 4, 9, 1, 5, 8, 12, 11, 10, 2};
        int k = 3;
        // output = {4,6,7,5,1,9,11,12,8,2,10}
        int i = 0;
        while (i + k < arr.length) {
            reverse(arr, i, i + k - 1);
            i += k;
        }
        reverse(arr, i, arr.length - 1);
        System.out.println(Arrays.toString(arr));
    } 
}
