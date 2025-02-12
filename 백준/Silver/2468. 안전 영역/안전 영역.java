import java.io.*;
import java.util.*;

public class Main {
    static int[] dx = {1, -1, 0, 0};
    static int[] dy = {0, 0, -1, 1};
    static int n;
    static int[][] board;
    static boolean[][] visited;
    static int ans = 0; // 최대 개수

    public static void main(String[] args) throws IOException {
        // 1. 입력 및 초기화
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine());
        board = new int[n][n];

        int mx = 0;
        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            for (int j = 0; j < n; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                mx = Math.max(mx, board[i][j]);
            }
        }
        for (int h = 0; h < mx; h++) {
            visited = new boolean[n][n];
            int cnt = 0; // 강수량에 따른 안전영역 개수
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    if (!visited[i][j] && board[i][j] > h) { // 방문 x, 높이가 h보다 높은 경우(침수 x)
                        bfs(i, j, h);
                        cnt++;
                    }
                }
                ans = Math.max(cnt, ans);
            }
        }
        System.out.println(ans);
    }

    public static void bfs(int x, int y, int hei) {
        Queue<int[]> q = new LinkedList<>();
        q.add(new int[]{x, y});
        visited[x][y] = true;

        while (!q.isEmpty()) {
            int cur[] = q.poll();
            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                if (nx >= 0 && nx < n && ny >= 0 && ny < n) {
                    if (!visited[nx][ny] && board[nx][ny] > hei) {
                        visited[nx][ny] = true;
                        q.add(new int[]{nx, ny});
                    }
                }
            }
        }
    }
}
