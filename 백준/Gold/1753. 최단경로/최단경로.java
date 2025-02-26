import java.io.*;
import java.util.*;

public class Main {
    public static class Node implements Comparable<Node> {
        int e;
        int v;

        public Node(int e, int v) {
            this.e = e;
            this.v = v;
        }

        @Override
        public int compareTo(Node n) {
            return this.v - n.v; // 가중치 크기 비교
        }
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int v = Integer.parseInt(st.nextToken());
        int e = Integer.parseInt(st.nextToken());
        int start = Integer.parseInt(br.readLine()); // 시작정점

        // 간선 정보 -> 인접리스트 저장
        ArrayList<Node>[] adjList = new ArrayList[v + 1];
        for (int i = 1; i <= v; i++) {
            adjList[i] = new ArrayList<Node>();
        }

        for (int i = 0; i < e; i++) {
            st = new StringTokenizer(br.readLine());

            // 시작, 도착, 가중치
            int from = Integer.parseInt(st.nextToken());
            int to = Integer.parseInt(st.nextToken());
            int wei = Integer.parseInt(st.nextToken());

            adjList[from].add(new Node(to, wei));
        }

        // 최단거리 갱신 테이블
        int[] table = new int[v + 1];

        Arrays.fill(table, Integer.MAX_VALUE); // 무한대로 초기화

        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.add(new Node(start, 0)); // 시작정점: 0
        table[start] = 0;

        while (!pq.isEmpty()) {
            Node cur = pq.poll();

            for (Node nxt : adjList[cur.e]) { // 다음 정점 탐색
                if (table[nxt.e] > table[cur.e] + nxt.v) { // 다음 노드까지의 최단 거리 > 현재까지 최단거리 + 다음 노드까지의 거리
                    table[nxt.e] = table[cur.e] + nxt.v; // 새로운 경로가 더 짧다면 업데이트
                    pq.add(new Node(nxt.e, table[nxt.e]));
                }
            }
        }
        for (int i = 1; i <= v; i++) {
            if (table[i] == Integer.MAX_VALUE) System.out.println("INF"); // 경로 없을때
            else
                System.out.println(table[i]);
        }
    }
}
