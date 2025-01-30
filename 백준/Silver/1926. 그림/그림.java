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

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
            }
        }
        // System.out.println(Arrays.deepToString(board));

        // 2. 맵에서 모든 그림 찾기 -> 이중 for문으로 bfs 시작점 찾아내기
        Queue<int[]> q = new LinkedList<>();

        // 방문처리
        boolean[][] visited = new boolean[n][m];

        // 상하좌우 이동
        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        // 그림 개수
        int picture = 0;
        // 그림 최댓값
        int mx = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {

                if (board[i][j] == 1 && !visited[i][j]) { // 그림 시작점 &&  방문체크!(bfs 하기 전)
                    picture += 1;

                    // 1. 상하좌우로 연결된 그림 찾기-> bfs 수행
                    q.offer(new int[]{i, j});
                    visited[i][j] = true; // 방문처리

                    int cur_area = 0; // 현재 그림 면적

                    while (!q.isEmpty()) {
                        cur_area++;
                        int[] cur = q.poll();

                        for (int d = 0; d < 4; d++) {
                            int nx = cur[0] + dx[d];
                            int ny = cur[1] + dy[d];
                            if (nx >= 0 && nx < n && ny >= 0 && ny < m) {
                                if (!visited[nx][ny] && board[nx][ny] != 0) {
                                    q.offer(new int[]{nx, ny});
                                    visited[nx][ny] = true;
                                }
                            }
                        }
                    }
                    mx = Math.max(mx, cur_area);
                } else { // 그림 아닐 때
                    continue;
                }
            }
        }
        System.out.println(picture + " " + mx);
    }
}