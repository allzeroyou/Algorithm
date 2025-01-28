import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 계단 개수
        int n = Integer.parseInt(br.readLine());

        // 계단 점수 저장
        int[] S = new int[n + 1];
        for (int i = 1; i <= n; i++) {
            int grade = Integer.parseInt(br.readLine());
            S[i] = grade;
        }

        // 1. dp 테이블 설정
        int[][] dp = new int[n + 1][3];

        // 3. 초기값 설정
        dp[1][1] = S[1];
        dp[1][0] = 0;
        // n이 2 이상 일때만!
        if(n>=2){
            dp[2][1] = S[2];
            dp[2][2] = S[1] + S[2];
        }

        // 2. 점화식 도출
        for (int k = 3; k <= n; k++) {
            dp[k][1] = Math.max(dp[k - 2][1], dp[k - 2][2]) + S[k];
            dp[k][2] = dp[k - 1][1] + S[k];
        }

        System.out.println(Math.max(dp[n][1], dp[n][2]));
    }
}
