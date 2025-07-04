
import java.util.Arrays;
import java.util.HashMap;

public class Morgan_Stanley_Interview_Prep {

    /*
     * Missing in Array
     * https://www.geeksforgeeks.org/problems/missing-number-in-array1416/1?
     */
    int missingNum(int arr[]) {
        int n = arr.length;
        int[] newarr = new int[n + 1];
        for (int num : arr) {
            newarr[num - 1] = 1;
        }
        for (int i = 0; i < newarr.length; i++) {
            if (newarr[i] == 0) {
                return i + 1;
            }
        }

        return n + 1;
    }

    /*
     * 1. Two Sum
     * https://leetcode.com/problems/two-sum/description/
     */
    public int[] twoSum(int[] nums, int target) {
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        for (int i = 0; i < nums.length; i++) {
            int diff = target - nums[i];
            if (hashmap.containsKey(diff)) {
                return new int[]{i, hashmap.get(diff)};
            }
            hashmap.put(nums[i], i);
        }
        return new int[]{};
    }

    class ListNode {

        int val;
        ListNode next;

        ListNode(int x) {
            val = x;
            next = null;
        }
    }

    /*
     * https://leetcode.com/problems/intersection-of-two-linked-lists/
     *  A  1 2 3 4 5️⃣ 6
     *  B  12 13 14 5️⃣ 6
     *  B => 5️⃣ A => 4
     *  B => 6 (null) A => at 5️⃣ 
     *  Now, set B = headA
     *  B => 1  A => 6 (null)
     *  Now set A = headB
     *  B => 2 A => 12
     *  B => 3 A = 13
     *  B => 4  A => 14
     *  b => 5️⃣  A => 5️⃣ (intersected)
     */
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode a = headA;
        ListNode b = headB;
        if (a == null || b == null) {
            return null;
        }

        while (a != b) {
            a = a == null ? headB : a.next;
            b = b == null ? headA : b.next;
        }
        return a;
    }

    /*
     * Remove Duplicates Sorted Array
     * https://www.geeksforgeeks.org/problems/remove-duplicate-elements-from-sorted-array/1?
     */
    public int removeDuplicates(int[] arr) {
        int index = 1;
        for (int i = 1; i < arr.length; i++) {
            if (arr[i] != arr[i - 1]) {
                arr[index++] = arr[i];
            }
        }
        return index;
    }

    /*
     * 121. Best Time to Buy and Sell Stock
     * https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
     */
    public int maxProfit(int[] prices) {
        int maxProfit = 0, maxStockPrice = 0;
        for (int i = prices.length - 1; i >= 0; i--) {
            maxStockPrice = Math.max(maxStockPrice, prices[i]);
            maxProfit = Math.max(maxProfit, maxStockPrice - prices[i]);
        }
        return maxProfit;
    }

    /*
     * 41. First Missing Positive
     * https://leetcode.com/problems/first-missing-positive/description/
     */
    public int firstMissingPositive(int[] nums) {

        for (int i = 0; i < nums.length; i++) {
            while (nums[i] > 0 && nums[i] <= nums.length && nums[nums[i] - 1] != nums[i]) {
                int temp = nums[nums[i] - 1];
                nums[nums[i] - 1] = nums[i];
                nums[i] = temp;
            }
        }
        System.out.println(Arrays.toString(nums));
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != i + 1) {
                return i + 1;
            }
        }
        return nums.length;
    }

    /*
     * 28. Find the Index of the First Occurrence in a String
     */
    public int strStr_sol_1(String haystack, String needle) {
        // Solution 1
        return haystack.indexOf(needle);
    }

    public int strStr_sol_2(String haystack, String needle) {
        // Solution 2
        int i = 0, j = 0, start = 0;
        while (i < haystack.length() && j < needle.length()) {
            if (haystack.charAt(i) == needle.charAt(j)) {
                i++;
                j++;
                if (j == needle.length()) {
                    return i - j;
                }
            } else {
                start++;
                i = start;
                j = 0;
            }
        }
        return -1;
    }

    public int strStr_sol_3(String haystack, String needle) {
        // Solution 3
        int n = haystack.length();
        int m = needle.length();
        if (m == 0) {
            return 0;
        }

        for (int i = 0; i < n - m; i++) {
            int j = 0;
            while (j < m && haystack.charAt(i + j) == needle.charAt(j)) {
                j++;
            }
            if (j == m) {
                return i;
            }
        }
        return -1;
    }

}
