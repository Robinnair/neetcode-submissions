class Solution {
    public int maxProduct(int[] nums) {
        int maxProd=nums[0];
        int minProd=nums[0];
        int ans=nums[0];
        for(int i=1;i<nums.length;i++){
            int num=nums[i];
            int tempmax=Math.max(num,Math.max(num*minProd,num*maxProd));
            int tempmin=Math.min(num,Math.min(num*minProd,num*maxProd));
            maxProd=tempmax;
            minProd=tempmin;
            ans=Math.max(ans,maxProd);
        }
        return ans;
    }
}
