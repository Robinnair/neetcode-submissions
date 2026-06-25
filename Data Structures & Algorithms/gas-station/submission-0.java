class Solution {
    public int canCompleteCircuit(int[] gas, int[] cost) {
        int totalcost=0;
        int totalgas=0;
        for(int i=0;i<gas.length;i++){
            totalcost+=cost[i];
            totalgas+=gas[i];
        }
        if(totalcost>totalgas){
            return -1;
        }
        int start=0;
        int tank=0;

        for(int i=0;i<gas.length;i++){
            tank+=gas[i]-cost[i];
            if(tank<0){
                start=i+1;
                tank=0;
            }
        }
        return start;
    }
}
