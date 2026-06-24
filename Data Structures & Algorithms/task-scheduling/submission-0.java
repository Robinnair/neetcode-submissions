class Solution {
    public int leastInterval(char[] tasks, int n) {
        int []freq= new int[26];
        for(char ch:tasks){
            freq[ch-'A']++;
        }
        int max_freq=0;
        for(int f:freq){
            max_freq=Math.max(max_freq,f);
        }
        int countmax=0;
        for(int f:freq){
            if(f==max_freq){
                countmax++;
            }
        }
        int frame=(max_freq-1)*(n+1)+countmax;
        return Math.max(frame,tasks.length);
    }
}
