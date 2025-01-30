import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 행, 열
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];

        // 거리 배열
        int[][] dist = new int[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                dist[i][j] = -1; // -1 로 초기화함으로서 방문 배열 따로 두지 x
            }
        }

        for (int i = 0; i < n; i++) {
            String line = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = line.charAt(j) - '0';
            }
        }
        // System.out.println(Arrays.deepToString(board));

        // bfs 수행하면서 거리 저장
        Queue<int[]> q = new LinkedList<>();

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        // 시작점을 큐에 넣는다
        q.offer(new int[]{0, 0}); // board: 0-based
        // 시작점을 방문 체크한다!
        dist[0][0] = 1;

        while (!q.isEmpty()) {

            int[] cur = q.poll();
            int cx = cur[0];
            int cy = cur[1];

            for (int i = 0; i < 4; i++) {
                int nx = cx + dx[i];
                int ny = cy + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                    if (dist[nx][ny] == -1 && board[nx][ny] == 1) {
                        q.offer(new int[]{nx, ny});

                        // 거리 갱신(현재까지의 거리 + 1)
                        dist[nx][ny] = dist[cx][cy] + 1;
                    }
                }
            }
        }
        System.out.println(dist[n - 1][m - 1]);
    }
}
