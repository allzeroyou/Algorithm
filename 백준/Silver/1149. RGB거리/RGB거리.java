import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 집 개수
        int n = Integer.parseInt(br.readLine());

        // 색칠 비용 저장
        int[] R = new int[n + 1];
        int[] G = new int[n + 1];
        int[] B = new int[n + 1];

        for (int i = 1; i <= n; i++) {
            // 한줄에 띄어쓰기 기준으로 R, G, B 쫘르륵
            // 1번째 요소: R, 2번째 요소: G, 3번째 요소: B 배열에 넣고자 함.
            StringTokenizer st = new StringTokenizer(br.readLine());

            R[i] = Integer.parseInt(st.nextToken());
            G[i] = Integer.parseInt(st.nextToken());
            B[i] = Integer.parseInt(st.nextToken());
        }

        // 1. dp 테이블 설정
        int[][] dp = new int[n + 1][3];

        // 3. 초기값 설정
        dp[1][0] = R[1];
        dp[1][1] = G[1];
        dp[1][2] = B[1];

        // 2. 점화식 도출
        for (int i = 2; i <= n; i++) {
            dp[i][0] = Math.min(dp[i - 1][1], dp[i - 1][2]) + R[i];
            dp[i][1] = Math.min(dp[i - 1][0], dp[i - 1][2]) + G[i];
            dp[i][2] = Math.min(dp[i - 1][1], dp[i - 1][0]) + B[i];
        }

        // 답 도출
        int tmp = Math.min(dp[n][0], dp[n][1]);
        System.out.println(Math.min(tmp, dp[n][2]));
    }
}
