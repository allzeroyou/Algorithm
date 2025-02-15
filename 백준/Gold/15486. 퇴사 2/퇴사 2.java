import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        // 일 걸리는 시간
        int[] t = new int[n];
        // 이익
        int[] p = new int[n];

        for (int i = 0; i < n; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            t[i] = Integer.parseInt(st.nextToken());
            p[i] = Integer.parseInt(st.nextToken());
        }

        // 1. dp 테이블: 이익 최댓값 저장
        int[] dp = new int[n + 1];

        // 2. 초기값 설정

        // 3. 점화식
        for (int i = 0; i < n; i++) {
            // 다음날
            int nxtDay = i + t[i]; // 현재 날짜 + 일이 끝나는 날짜

            // 현재 작업 수행
            if (nxtDay <= n) { // n+1 일째는 불가
                dp[nxtDay] = Math.max(dp[i] + p[i], dp[nxtDay]);
            }
            // 현재 작업 수행 x -> 일이 끝나는 날에 이익 얻음
            dp[i + 1] = Math.max(dp[i + 1], dp[i]);
        }
        System.out.println(dp[n]);
    }
}
