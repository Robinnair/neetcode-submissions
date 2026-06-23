class Solution {
    public int[][] kClosest(int[][] points, int k) {
        PriorityQueue<int []> heap=new PriorityQueue<>((a,b)->(a[0]-b[0]));
        for(int [] p:points){
            int dist=p[0]*p[0]+p[1]*p[1];
            heap.add(new int[]{dist,p[0],p[1]});
        }
        int [][]ans= new int[k][2];
        for(int i=0;i<k;i++){
            int[] cur=heap.poll();
            ans[i][0]=cur[1];
            ans[i][1]=cur[2];
        }
        return ans;
    }
}
