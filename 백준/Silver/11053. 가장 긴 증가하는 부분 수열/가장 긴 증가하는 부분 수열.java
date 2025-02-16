import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 수열
        int[] a = new int[n];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        // dp 테이블: n일때 최대길이
        int[] dp = new int[n + 1];
        int ans = 1; // 초기값
        Arrays.fill(dp, 1); // 모든 수열의 요소는 각 1의 길이를 가짐

        for (int i = 1; i < n; i++) {// 1-based
            for (int j = 0; j < i; j++) { // 수열이 증가해야 하므로 2중 for문 사용한다
                if (a[i] > a[j]) {
                    dp[i] = Math.max(dp[i], dp[j] + 1);
                }
                ans = Math.max(ans, dp[i]);
            }
        }
        System.out.println(ans);
    }
}
