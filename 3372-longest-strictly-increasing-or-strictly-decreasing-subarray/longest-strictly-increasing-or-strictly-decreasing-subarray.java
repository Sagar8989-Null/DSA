class Solution {

    private int lenCount(int[] nums, int i) {

        int n = nums.length;
        int count = 1;

        boolean increasing = nums[i] < nums[i + 1];

        for (int j = i; j < n - 1; j++) {

            if (increasing && nums[j] < nums[j + 1]) {
                count++;
            }
            else if (!increasing && nums[j] > nums[j + 1]) {
                count++;
            }
            else {
                break;
            }
        }

        return count;
    }

    public int longestMonotonicSubarray(int[] nums) {

        int n = nums.length;

        if (n == 1) return 1;

        int max = 1;

        for (int i = 0; i < n - 1; i++) {
            max = Math.max(max, lenCount(nums, i));
        }

        return max;
    }
}