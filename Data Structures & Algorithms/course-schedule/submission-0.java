class Solution {

    boolean dfs(int node,
                List<Integer>[] graph,
                boolean[] visited,
                boolean[] inPath) {

        if (inPath[node]) {
            return true;
        }

        if (visited[node]) {
            return false;
        }

        visited[node] = true;
        inPath[node] = true;

        for (int neighbor : graph[node]) {
            if (dfs(neighbor, graph, visited, inPath)) {
                return true;
            }
        }

        inPath[node] = false;
        return false;
    }

    public boolean canFinish(int numCourses, int[][] prerequisites) {

        List<Integer>[] graph = new ArrayList[numCourses];

        for (int i = 0; i < numCourses; i++) {
            graph[i] = new ArrayList<>();
        }

        for (int[] edge : prerequisites) {
            int course = edge[0];
            int prereq = edge[1];

            graph[prereq].add(course);
        }

        boolean[] visited = new boolean[numCourses];
        boolean[] inPath = new boolean[numCourses];

        for (int i = 0; i < numCourses; i++) {
            if (dfs(i, graph, visited, inPath)) {
                return false;
            }
        }

        return true;
    }
}