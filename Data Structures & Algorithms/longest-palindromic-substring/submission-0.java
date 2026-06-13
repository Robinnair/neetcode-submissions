class Solution {
    public String longestPalindrome(String s) {
        int n=s.length();
        Boolean [][]dp= new Boolean[n][n];
        int max_length=0;
        int start=-1;
        for(int i=0;i<n;i++){
            for(int j=i;j<n;j++){
                if(solver(i,j,s,dp)){
                    int length=j-i+1;
                    if(length>max_length){
                        max_length=length;
                        start=i;
                    }
                }
            }
        }
        return s.substring(start,start+max_length);
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
