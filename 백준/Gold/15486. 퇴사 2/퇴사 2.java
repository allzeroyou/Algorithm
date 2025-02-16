import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 시간, 이익 저장
        int[] t = new int[n];
        int[] p = new int[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            t[i] = Integer.parseInt(st.nextToken());
            p[i] = Integer.parseInt(st.nextToken());
        }

        // dp 테이블: n일째 최대이익
        int[] dp = new int[n + 1];

        for (int i = 0; i < n; i++) {
            int nxtDay = i + t[i];

            if (nxtDay <= n) {
                dp[nxtDay] = Math.max(dp[nxtDay], dp[i] + p[i]);
            }
            // 일이 끝날때까지 이익 누적
            if (i <= n) { // 마지막 날이 아닐때만 다음 날로 이익 이월시킨다!
                dp[i + 1] = Math.max(dp[i + 1], dp[i]);
            }
        }

        System.out.println(dp[n]);
    }
}
