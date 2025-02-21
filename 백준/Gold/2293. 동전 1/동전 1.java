import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int n = Integer.parseInt(st.nextToken());
        int k = Integer.parseInt(st.nextToken());

        // 동전 가치
        int[] coins = new int[n+1];

        for (int i = 1; i <= n; i++) {
            coins[i] = Integer.parseInt(br.readLine());
        }

        // 1. dp 테이블
        int[] dp = new int[10001]; // n의 최댓값

        // 2. 초기값
        dp[0] = 1; // 0을 만드는 경우의 수는 1가지

        // 3. 점화식
        for (int i = 1; i <= n; i++) {
            for (int j = coins[i]; j <= k; j++) {
                dp[j] += dp[j - coins[i]];
            }
        }
        System.out.println(dp[k]);
    }
}
