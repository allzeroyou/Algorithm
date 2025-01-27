import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int n = Integer.parseInt(br.readLine());

        // 1. 테이블 정의
        int[] dp = new int[n + 1];

        // 3. 초기값 설정
        dp[1] = 0;

        // 2. 점화식
        for (int i = 2; i <= n; i++) {
            // 기본적으로 1을 뺀 경우 고려
            dp[i] = dp[i - 1] + 1;
            // 2로 나눠지는 경우 최솟값 비교
            if (i % 2 == 0) {
                dp[i] = Math.min(dp[i / 2] + 1, dp[i]);
            }
            // 3으로 나눠지는 경우 최솟값 비교
            if (i % 3 == 0) {
                dp[i] = Math.min(dp[i / 3] + 1, dp[i]);
            }
        }
        System.out.println(dp[n]);
    }
}
