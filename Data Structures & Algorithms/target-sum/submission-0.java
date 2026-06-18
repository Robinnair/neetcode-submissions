class Solution {
    HashMap<String,Integer> dp;
    int actual_target;
    public int findTargetSumWays(int[] nums, int target) {
        dp=new HashMap<>();
        actual_target=target;
        return solver(0,0,nums);
    }

    private int solver(int i,int current,int []nums){
        if(i==nums.length){
            return (current==actual_target)? 1:0;
        }
        String key=i+","+current;
        if(dp.containsKey(key)){
            return dp.get(key);
        }
        int sub=solver(i+1,current-nums[i],nums);
        int sum=solver(i+1,current+nums[i],nums);
        dp.put(key,sub+sum);
        return sub+sum;
    }
}
