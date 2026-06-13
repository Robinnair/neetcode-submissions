class Solution {
    public int countSubstrings(String s) {
        int n=s.length();
        Boolean [][]dp= new Boolean[n][n];
        int count=0;
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(solver(i,j,s,dp)){
                    count++;
                }
            }
        }
        return count;
    }

    private Boolean solver(int i,int j,String s,Boolean [][]dp){
        if(i>=j){
            return true;
        }
        if(dp[i][j]!=null){
            return dp[i][j];
        }
        if(s.charAt(i)!=s.charAt(j)){
            dp[i][j]=false;
            return dp[i][j];
        }
        dp[i][j]=solver(i+1,j-1,s,dp);
        return dp[i][j];
    }
}
