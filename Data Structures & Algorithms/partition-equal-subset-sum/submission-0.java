class Solution {
    Boolean [][]dp;
    public boolean canPartition(int[] nums) {
        int n=nums.length;
        int sum=0;
        for(int num:nums){
            sum+=num;
        }
        if(sum%2==1){
            return false;
        }
        int target=sum/2;
        dp= new Boolean[n][target+1];
        return solver(0,target,nums);
    }

    private boolean solver(int i,int target,int []nums){
        if(target==0){
            return true;
        }
        if(i==nums.length){
            return false;
        }
        if(dp[i][target]!=null){
            return dp[i][target];
        }
        boolean skip=solver(i+1,target,nums);
        boolean take=false;
        if(nums[i]<=target){
            take=solver(i+1,target-nums[i],nums);
        }
        dp[i][target]=(take||skip);
        return dp[i][target];
    }
}
