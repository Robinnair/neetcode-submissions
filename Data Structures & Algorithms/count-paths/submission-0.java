class Solution {
    Integer [][]dp;
    public int uniquePaths(int m, int n) {
        dp=new Integer [m+1][n+1];
        return solver(0,0,m,n);
    }
    private int solver(int i,int j,int m,int n){
        if(i==m-1 && j==n-1){
            return 1;
        }
        if(i>=m||j>=n){
            return 0;
        }
        if(dp[i][j]!=null){
            return dp[i][j];
        }
        int down=solver(i+1,j,m,n);
        int right=solver(i,j+1,m,n);
        return dp[i][j]=down+right;
    }
}
