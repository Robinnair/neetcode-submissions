class Solution {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap= new PriorityQueue<>((a,b)->b-a);
        for(int num:nums){
            heap.add(num);
        }
        int output=0;
        while(k!=0){
            k--;
            output=heap.poll();
        }
        return output;
    }
}
