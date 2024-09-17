
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    // 방향 나타내는 상수
    static int up = 0;
    static int right = 1;
    static int down = 2;
    static int left = 3;

    // cctv 회전 경우의 수
    static int[][][] cctvDir = {
            {}, // 0번 cctv 없음
            {{up}, {right}, {down}, {left}}, // 1번
            {{left, right}, {up, down}}, // 2번
            {{up, right}, {down, right}, {left, down}, {left, up}}, // 3번
            {{left, up, right}, {up, right, down}, {right, down, left}, {down, left, up}}, // 4번
            {{up, right, down, left}}, // 5번
    };
    // cctv 정보
    static List<CCTV> cctvList = new ArrayList<>();
    static int answer = Integer.MAX_VALUE; // 최솟값 출력
    // n,m 전역변수화
    static int n;
    static int m;

    public static void main(String[] args) throws IOException {
        // 사무실, cctv 정보 -> cctv 방향 바꾸면서 사각지대 최소 크기?
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken());
        m = Integer.parseInt(st.nextToken());

        int[][] board = new int[n][m];

        for (int i = 0; i < n; i++) {
            st = new StringTokenizer(br.readLine());
            for (int j = 0; j < m; j++) {
                board[i][j] = Integer.parseInt(st.nextToken());
                // cctv 위치 저장
                if (board[i][j] >= 1 && board[i][j] <= 5) {
                    cctvList.add(new CCTV(i, j, board[i][j]));
                }
            }
        }
        // board순회하면서 가장 최소의 사각지대일때의 경우의 수 찾기
        dfs(0, board);
        System.out.println(answer);
    }

    static void dfs(int depth, int[][] curBoard) { // 현재 처리중인 cctv 인덱스, 현재 사무실 상태
        // dfs 종료조건: cctv를 다 돌았을때
        if (depth == cctvList.size()) {
            // 사각지대 개수 세기
            answer = Math.min(answer, countBlind(curBoard));
            return;
        }
        CCTV cctv = cctvList.get(depth);
        for (int[] dir : cctvDir[cctv.type]) {
            int[][] nextBoard = deepCopy(curBoard);
            // cctv의 감시영역을 board에 표시
            watch(nextBoard, cctv, dir);
            dfs(depth + 1, nextBoard);
        }
    }

    static int countBlind(int[][] curBoard) { // 사각지대 개수 세기
        int cnt = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (curBoard[i][j] == 0) {
                    cnt++;
                }
            }
        }
        return cnt;
    }

    static int[][] deepCopy(int[][] original) { // 깊은 복사용
        int n = original.length;
        int m = original[0].length;
        int[][] copy = new int[n][m];

        for (int i = 0; i < n; i++) {
            System.arraycopy(original[i], 0, copy[i], 0, original[i].length);
        }
        return copy;
    }

    static void watch(int[][] board, CCTV cctv, int[] dir) {
        // 4방향 탐색
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        for (int d : dir) {
            int nx = cctv.x;
            int ny = cctv.y;

            while (true) { // 해당 방향으로 계속 진행!
                nx += dx[d];
                ny += dy[d];
                if (nx < 0 || nx >= n || ny < 0 || ny >= m || board[nx][ny] == 6) { // 경계를 벗어나거나 벽일 경우 stop
                    break;
                }
                if (board[nx][ny] == 0) {
                    board[nx][ny] = -1; // 감시 영역임!
                }
            }
        }
    }
}

// CCTV 클래스 정의
class CCTV {
    int x;
    int y;
    int type;

    // 생성자
    CCTV(int x, int y, int type) {
        this.x = x;
        this.y = y;
        this.type = type;
    }
}