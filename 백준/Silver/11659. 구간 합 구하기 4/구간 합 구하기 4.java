
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // n m
        String ln1 = br.readLine();
        StringTokenizer st = new StringTokenizer(ln1, " ");

        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());

        // 1. dp 테이블 설정
        int[] dp = new int[n + 1];
        String ln2 = br.readLine();
        StringTokenizer st2 = new StringTokenizer(ln2, " ");

        for (int i = 1; i <= n; i++) {
            dp[i] = dp[i - 1] + Integer.parseInt(st2.nextToken());
        }

        // 3. 초기값 설정
        // 1인 경우 예외처리 해준다!
        if (n == 1) {
            System.out.println(dp[1]);
            return;
        }

        // 2. 점화식 도출: 구간 합 구하기
        for (int k = 0; k < m; k++) {
            String ln3 = br.readLine();
            StringTokenizer st3 = new StringTokenizer(ln3, " ");
            int i = Integer.parseInt(st3.nextToken());
            int j = Integer.parseInt(st3.nextToken());

            // 답 도출
            System.out.println(dp[j] - dp[i - 1]);
        }
    }
}
