class Solution {
    private boolean dfs(int node,List<Integer>[] graph,boolean visited[],boolean inpath[],List<Integer> order){
        if(inpath[node]){
            return true;
        }
        if(visited[node]){
            return false;
        }
        inpath[node]=true;
        visited[node]=true;
        for(int neighbour:graph[node]){
            if(dfs(neighbour,graph,visited,inpath,order)){
                return true;
            }
        }
        inpath[node]=false;
        order.add(node);
        return false;
    }
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        List<Integer>[] graph= new ArrayList[numCourses];
        for(int i=0;i<numCourses;i++){
            graph[i]=new ArrayList<>();
        }

        for(int[] edge:prerequisites){
            int course=edge[0];
            int prereq=edge[1];
            graph[prereq].add(course);
        }
        boolean visited[]= new boolean[numCourses];
        boolean inpath[]=new boolean[numCourses];
        List<Integer> order= new ArrayList<>();

        for(int i=0;i<numCourses;i++){
            if(dfs(i,graph,visited,inpath,order)){
                return new int[0];
            }
        }
        Collections.reverse(order);
        int result[]=new int[numCourses];

        for(int i=0;i<numCourses;i++){
            result[i]=order.get(i);
        }

        return result;
    }
}
