import java.io.*;
import java.util.*;

public class Main {
    static boolean[][] board;
    static boolean[] visited;
    static int n, m;
    static int answer;

    public static void dfs(int idx) {
        answer++; //
        visited[idx] = true; // 방문처리

        for (int i = 1; i <= n; i++) {
            if (!visited[i] && board[idx][i])
                dfs(i);
        }
    }

    public static void main(String args[]) throws IOException {
        // 1. 입력 및 초기화
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // v, e
        n = Integer.parseInt(br.readLine());
        m = Integer.parseInt(br.readLine());

        board = new boolean[n + 1][n + 1]; // vertex
        visited = new boolean[n + 1];

        // 2. 그래프 정보
        int x, y;

        for (int i = 0; i < m; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            x = Integer.parseInt(st.nextToken());
            y = Integer.parseInt(st.nextToken());
            board[x][y] = board[y][x] = true; // 양방향
        }

        // 3. dfs
        dfs(1); // 1번노드부터 시작

        // 4. 정답 출력
        System.out.println(answer - 1); // 1번 노드는 제외시킴(바이러스 퍼지게 되는 컴퓨터 수 반환)
    }
}
