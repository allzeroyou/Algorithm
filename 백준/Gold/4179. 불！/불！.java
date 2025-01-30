import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        // 행, 열
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        char[][] board = new char[n][m]; // #: 벽, J: 지훈, F: 불, .: 이동 가능칸

        for (int i = 0; i < n; i++) {
            String li = br.readLine();
            for (int j = 0; j < m; j++) {
                board[i][j] = li.charAt(j);
            }
        }
        // System.out.println(Arrays.deepToString(board));
        Queue<int[]> fq = new LinkedList<>(); // 불 dfs 용 큐
        Queue<int[]> jq = new LinkedList<>(); // 지훈 dfs 용 큐

        int[][] fdis = new int[n][m]; // 불 전파 시간 저장용
        int[][] jdis = new int[n][m]; // 지훈이 이동 시간 저장용

        int[] dx = {1, -1, 0, 0};
        int[] dy = {0, 0, -1, 1};

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                fdis[i][j] = -1;
                jdis[i][j] = -1;
                if (board[i][j] == 'F') {
                    fq.offer(new int[]{i, j});
                    fdis[i][j] = 0; // 현재 지점은 방문 처리해줘야
                } else if (board[i][j] == 'J') {
                    jq.offer(new int[]{i, j});
                    jdis[i][j] = 0;
                }
            }
        }
        // 불 bfs
        while (!fq.isEmpty()) {
            int[] cur = fq.poll();

            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                // 범위 내, 방문 x, 갈 수 있다면
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || fdis[nx][ny] != -1 || board[nx][ny] == '#') continue;

                fq.offer(new int[]{nx, ny});
                fdis[nx][ny] = fdis[cur[0]][cur[1]] + 1;
            }
        }
        // System.out.println(Arrays.deepToString(fdis));

        // 지훈 bfs
        while (!jq.isEmpty()) {
            int[] cur = jq.poll();

            for (int i = 0; i < 4; i++) {
                int nx = cur[0] + dx[i];
                int ny = cur[1] + dy[i];
                // 범위 벗어났다면 -> 탈출한거!
                if (nx < 0 || nx >= n || ny < 0 || ny >= m) {
                    System.out.println(jdis[cur[0]][cur[1]] + 1); // 현재 + 1
                    return;
                }
                if (jdis[nx][ny] != -1 || board[nx][ny] == '#') continue;
                // 지훈 이동 시간 > 불 이동 시간이라면 해당 칸 가지 못함!
                if (fdis[nx][ny] != -1 && jdis[cur[0]][cur[1]] + 1 >= fdis[nx][ny]) continue;

                jq.offer(new int[]{nx, ny});
                jdis[nx][ny] = jdis[cur[0]][cur[1]] + 1;
            }
        }
        // 여기까지 왔다면,, 탈출 실패
        System.out.println("IMPOSSIBLE");
    }
}
