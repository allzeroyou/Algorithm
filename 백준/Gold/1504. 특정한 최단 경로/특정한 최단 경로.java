
import java.io.*;
import java.util.*;

// 무방향(양방향) 그래프
// 1번 정점 -> n번 정점으로 이동시, 최단 경로 길이?
// 없을 땐 -1 출력

// 주어진 두 정점은 반드시 통과하도록
// 이동했던 정점, 간선 다시 이동 가능!
// 지나야 하는 정점 기준으로 2번 다익스트라 실행

public class Main {
    static int n;
    static List<Node>[] adj;
    static int[] esst = new int[2];
    static int[] dist;
    static int INF = 200000 * 1000; // 오버플로우 방지

    private static class Node implements Comparable<Node> {
        int num;
        int len;

        public Node(int num, int len) {
            this.num = num;
            this.len = len;
        }

        @Override
        public int compareTo(Node n) {
            return this.len > n.len ? 1 : -1;
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken()); // 정점 개수
        int e = Integer.parseInt(st.nextToken()); // 간선 개수

        // 거리 저장-> 인접리스트
        adj = new ArrayList[n + 1]; // 정점: 1부터 시작
        for (int i = 1; i < n + 1; i++) {
            adj[i] = new ArrayList<>();
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());

            int from = Integer.parseInt(st.nextToken()); // from: 시작 정점
            int to = Integer.parseInt(st.nextToken()); // to: 도착 정점
            int dist = Integer.parseInt(st.nextToken()); // 거리

            adj[from].add(new Node(to, dist));
            adj[to].add(new Node(from, dist));
        }
        // 필수로 거쳐야 하는 정점 입력
        st = new StringTokenizer(br.readLine());
        esst[0] = Integer.parseInt(st.nextToken()); // node1
        esst[1] = Integer.parseInt(st.nextToken()); // node2
        // 입력 끝

        // 거리 배열
        dist = new int[n + 1];

        // 1. 1-> node1 -> node2 -> n
        int ans1 = 0;
        ans1 += Dijkstra(1, esst[0]);
        ans1 += Dijkstra(esst[0], esst[1]);
        ans1 += Dijkstra(esst[1], n);

        // 2. 1-> node2 -> node 1 -> n
        int ans2 = 0;
        ans2 += Dijkstra(1, esst[1]);
        ans2 += Dijkstra(esst[1], esst[0]);
        ans2 += Dijkstra(esst[0], n);

        int ans = ans1 >= INF && ans2 >= INF ? -1 : Math.min(ans1, ans2);

        System.out.println(ans);
    }

    private static int Dijkstra(int start, int end) {
        Arrays.fill(dist, INF);
        boolean[] visited = new boolean[n + 1]; // 정점은 1부터 시작

        PriorityQueue<Node> pq = new PriorityQueue<>();

        // 시작점 추가
        pq.offer(new Node(start, 0));
        dist[start] = 0;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            if (visited[cur.num]) continue;

            visited[cur.num] = true;

            for (int i = 0; i < adj[cur.num].size(); i++) {
                Node nxt = adj[cur.num].get(i);

                if (dist[nxt.num] > dist[cur.num] + nxt.len) {
                    dist[nxt.num] = dist[cur.num] + nxt.len;
                    pq.offer(new Node(nxt.num, dist[nxt.num]));
                }
            }
        }
        return dist[end];
    }
}
