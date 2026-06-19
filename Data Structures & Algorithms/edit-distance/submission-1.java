class Solution {
    Integer [][]dp;
    public int minDistance(String word1, String word2) {
        dp= new Integer [word1.length()+1][word2.length()+1];
        return solver(0,0,word1,word2);
    }

    private int solver(int i,int j,String word1,String word2){
        if(i==word1.length() && j==word2.length()){
            return 0;
        }
        if (i == word1.length())
            return word2.length() - j;

        if (j == word2.length())
            return word1.length() - i;

        if(dp[i][j]!=null){
            return dp[i][j];
        }

        if(word1.charAt(i)==word2.charAt(j)){
            return dp[i][j]=solver(i+1,j+1,word1,word2);
        }
        else{
            int insert=1+solver(i,j+1,word1,word2);
            int delete=1+solver(i+1,j,word1,word2);
            int replace=1+solver(i+1,j+1,word1,word2);
            return dp[i][j]=Math.min(insert,Math.min(delete,replace));
        }
    }
}
