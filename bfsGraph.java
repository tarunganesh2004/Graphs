import java.util.*;

public class bfsGraph {
    public static void main(String[] args) {
        // taking graph as adjacency List
        int v = 5;
        List<List<Integer>> adjList = new ArrayList<>();
        for (int i = 0; i < v; i++) {
            adjList.add(new ArrayList<>());
        }

        // Example graph {0-->1,0-->2,1-->3,1-->4}
        adjList.get(0).add(1);
        adjList.get(0).add(2);
        adjList.get(1).add(3);
        adjList.get(1).add(4); // directed graph

        bfs(v, adjList, 0);
    }

    public static void bfs(int v, List<List<Integer>> adjList, int start) {
        boolean[] vis = new boolean[v];
        Queue<Integer> q = new LinkedList<>();
        q.add(start);
        vis[start] = true;
        while (!q.isEmpty()) {
            int cur = q.poll();
            System.out.print(cur + " ");
            for (int neighbour : adjList.get(cur)) {
                if (!vis[neighbour]) {
                    q.add(neighbour);
                    vis[neighbour] = true;
                }
            }
        }
    }
}
