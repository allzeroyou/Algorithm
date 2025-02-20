
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 1. dp 테이블
        int[] dp = new int[1000001]; // 배열 사이즈 최댓값

        // 2. 초기값
        dp[1] = 1;
        dp[2] = 2;

        // 3. 점화식
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i - 2] + dp[i - 1]) % 15746;
        }
        System.out.println(dp[n]);
    }
}
