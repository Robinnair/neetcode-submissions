class Solution {
    Integer [][]dp;
    public int maxProfit(int[] prices) {
        dp=new Integer [prices.length+1][2];
        return dfs(0,1,prices);
    }
    private int dfs(int i,int buying,int[] prices){
        if(i>=prices.length){
            return 0;
        }
        if(dp[i][buying]!=null){
            return dp[i][buying];
        }
        int profit=-1;
        if(buying==1){
            int take=-prices[i]+dfs(i+1,0,prices);
            int skip=dfs(i+1,1,prices);
            profit=Math.max(take,skip);
        }
        else{
            int sell=prices[i]+dfs(i+2,1,prices);
            int hold=dfs(i+1,0,prices);
            profit=Math.max(sell,hold);
        }
        dp[i][buying]=profit;
        return dp[i][buying];
        
    }
}
