class Solution {
    public int lastStoneWeight(int[] stones) {
        PriorityQueue<Integer> heap= new PriorityQueue<>((a,b)->b-a);
        for(int s:stones){
            heap.add(s);
        }
        while(heap.size()>1){
            int s1=heap.poll();
            int s2=heap.poll();
            if(s1>s2){
                int new_stone=s1-s2;
                heap.add(new_stone);
            }
        }
        if(heap.size()==1){
            return heap.poll();
        }
        return 0;
    }
}
