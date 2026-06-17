class Solution {
    int [][]dp;
    public int longestCommonSubsequence(String text1, String text2) {
        dp= new int[text1.length()+1][text2.length()+1];
        for(int i=0;i<text1.length();i++){
            for(int j=0;j<text2.length();j++){
                dp[i][j]=-1;
            }
        }
        return lcs(0,0,text1,text2);
    }
    private int lcs(int i,int j,String text1,String text2){
        if(i==text1.length()||j==text2.length()){
            return 0;
        }
        if(dp[i][j]!=-1){
            return dp[i][j];
        }
        if(text1.charAt(i)==text2.charAt(j)){
            dp[i][j]=1+lcs(i+1,j+1,text1,text2);
            return dp[i][j];
        }
        else{
            dp[i][j]=Math.max(lcs(i+1,j,text1,text2),lcs(i,j+1,text1,text2));
            return dp[i][j];
        }
    }
}
