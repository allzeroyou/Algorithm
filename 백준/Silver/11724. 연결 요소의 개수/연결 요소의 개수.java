
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.StringTokenizer;

public class Main {
    // 방문 배열
    static boolean visited[];
    // 인접리스트
    static ArrayList<Integer>[] arr;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        visited = new boolean[n + 1]; // 1부터 시작
        arr = new ArrayList[n + 1];

        // 인접리스트의 각 ArrayList 초기화
        for (int i = 1; i < n + 1; i++) {
            arr[i] = new ArrayList<Integer>();
        }
        // 인접리스트에 그래프 데이터 저장
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            // 무방향성 그래프
            arr[s].add(e);
            arr[e].add(s);
        }
        // 연결 개수 카운트
        int cnt = 0;
        for (int i = 1; i < n+1; i++) {
            if (!visited[i]) {
                cnt++;
                DFS(i);
            }
        }
        System.out.println(cnt);
    }

    private static void DFS(int v) {
        if (visited[v]) { // 방문노드라면 함수 종료
            return;
        }
        visited[v] = true;
        for (int i : arr[v]) { // 현재 노드에서 연결된 노드 탐색
            if (!visited[i]) {
                DFS(i); // 재귀함수
            }
        }
    }
}
