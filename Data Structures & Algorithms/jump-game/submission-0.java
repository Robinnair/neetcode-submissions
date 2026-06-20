class Solution {
    boolean []dp;
    public boolean canJump(int[] nums) {
        dp= new boolean[nums.length];
        if(nums.length==1){
            return true;
        }
        dp[0]=true;
        for(int i=0;i<nums.length;i++){
            if(!dp[i]){
                continue;
            }
            for(int j=1;j<=nums[i]&&i+j<nums.length;j++){
                dp[i+j]=true;
            }
        }
        return dp[nums.length-1];
    }
}
