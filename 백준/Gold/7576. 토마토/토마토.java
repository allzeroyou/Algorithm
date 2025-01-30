import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 행, 열
        int m = Integer.parseInt(st.nextToken());
        int n = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // System.out.println(Arrays.deepToString(board));

        // # 예외처리1: 모든 토마토 익었는지 체크/ 익은 토마토를 큐에 넣는다
        Queue<int[]> q = new LinkedList<>();
        // 거리 배열
        int[][] dist = new int[n][m];

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        int cnt = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0) {
                    cnt++;
                    dist[i][j] = -1; // -1로 초기화해준다
                } else if (board[i][j] == 1) {
                    q.offer(new int[]{i, j});
                }
            }
        }

        if (cnt == 0) {
            System.out.println(0);
            return;
        }

        while (!q.isEmpty()) {
            int[] cur = q.poll();

            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];

                if (nx >= 0 && nx < n && ny >= 0 && ny < m && dist[nx][ny] == -1 && board[nx][ny] == 0) {
                    q.offer(new int[]{nx, ny});
                    dist[nx][ny] = dist[cur[0]][cur[1]] + 1; // 거리 +1
                    board[nx][ny] = 1; // 토마토 익기
                }
            }
        }
        // bfs를 모두 돌았는데도 0이 남아있는 경우
        int ans = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (board[i][j] == 0) {
                    System.out.println(-1);
                    return;
                }
                ans = Math.max(ans, dist[i][j]); // 다 익을 때 까지 걸리는 날짜
            }
        }

        System.out.println(ans);
    }
}
