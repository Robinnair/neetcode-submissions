class Solution {
    Integer [][]dp;
    public int lengthOfLIS(int[] nums) {
        int n=nums.length;
        dp= new Integer[n][n+1];
        return solver(0,-1,nums);
    }

    private int solver(int i,int prev,int []nums){
        if(i==nums.length){
            return 0;
        }
        if(dp[i][prev+1]!=null){
            return dp[i][prev+1];
        }
        int skip=solver(i+1,prev,nums);
        int take=0;
        if(prev==-1||nums[i]>nums[prev]){
            take=1+solver(i+1,i,nums);
        }
        dp[i][prev+1]=Math.max(take,skip);
        return dp[i][prev+1];
    }
}
