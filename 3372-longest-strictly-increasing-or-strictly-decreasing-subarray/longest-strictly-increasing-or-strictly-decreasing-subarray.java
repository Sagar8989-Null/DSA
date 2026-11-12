class Solution {

    public int longestMonotonicSubarray(int[] nums) {
        int countD = 1;
        int countI = 1;
        int max = 1;

        for(int i = 1; i < nums.length; i ++){

            if (nums[i] < nums[i-1]){
                countD++;
                countI = 1; 
            }

            else if(nums[i] > nums[i-1]){
                countI++;
                countD = 1;
            }
            
            else{
                countI = 1;
                countD = 1;
            }

            max = Math.max(max,Math.max(countI,countD));

        }

        return max;
    }
}