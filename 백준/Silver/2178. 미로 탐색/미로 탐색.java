
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.util.StringTokenizer;

public class Main {
    // 상하좌우 이동
    static int[] dx = {0, 1, 0, -1};
    static int[] dy = {-1, 0, 1, 0};
    // 방문 배열
    static boolean[][] visited;
    // 탐색 board
    static int[][] board;
    // 가로 x 세로
    static int n, m;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());
        board = new int[n][m];
        visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            // 공백 x
            String line = st.nextToken(); // 101111
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(line.substring(j, j + 1));
            }
        }
        // BFS
        BFS(0, 0); // 시작점
        System.out.println(board[n - 1][m - 1]); // idx
    }

    private static void BFS(int i, int j) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[]{i, j}); // (0,0)
        while (!q.isEmpty()) {
            int now[] = q.poll();
            visited[i][j] = true;
            for (int k = 0; k < 4; k++) { // 상하좌우 탐색
                int x = now[0] + dx[k];
                int y = now[1] + dy[k];
                if (x >= 0 && y >= 0 && x < n && y < m) { // 배열 안이거나
                    if (board[x][y] != 0 && !visited[x][y]) {
                        // 칸이 1이거나 방문 하지 않았을 경우
                        visited[x][y] = true;
                        board[x][y] = board[now[0]][now[1]] + 1; // 최단경로 갱신
                        q.add(new int[]{x, y});
                    }
                }
            }
        }
    }
}
