import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // n
        int n = Integer.parseInt(br.readLine());

        // 1. dp 테이블 설정
        int[] dp = new int[n + 1];
        int[] pre = new int[n + 1]; // dp[i]가 최솟값을 만들게 한 직전 값 저장용

        // 3. 초기값 설정
        dp[1] = 0;
        pre[1] = 0;

        // 2. 점화식 도출

        // 만드는 데 걸린 경로 값 출력
        for (int i = 2; i <= n; i++) {
            // 1을 빼준다.
            dp[i] = dp[i - 1] + 1; // dp[4]=dp[3]+1 = 2
            pre[i] = i - 1; // pre[4]=3;

            // 2로 나눠지면 2로 나눈다 -> 최솟값이 저장되어야 하므로 2로 나눈 값이 더 작으면 갱신
            if (i % 2 == 0 && dp[i] > dp[i / 2] + 1) { // dp[4] > dp[2]+1
                dp[i] = dp[i / 2] + 1;
                pre[i] = i / 2;
            }

            // 3으로 나눠지면 3으로 나눈다
            if (i % 3 == 0 && dp[i] > dp[i / 3] + 1) {
                dp[i] = dp[i / 3] + 1;
                pre[i] = i / 3;
            }
        }
        // 연산 횟수 출력
        System.out.println(dp[n]);

        // 경로 값 출력
        int cur = n;
        StringBuilder sb = new StringBuilder();

        while (true) {
            sb.append(cur).append(" ");
            if (cur == 1) break;
            cur = pre[cur];
        }
        System.out.print(sb.toString().trim()); // 마지막 숫자에 붙인 공백 지움(trim: 문자열 양 끝의 불필요한 공백 지움)
    }
}