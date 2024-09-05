
import java.util.Scanner;

public class Main {
    static int n, k;
    static int dp[][];

    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);

        n = sc.nextInt();
        k = sc.nextInt();

        dp = new int[n + 1][n + 1];
        // dp 테이블 초기화
        for (int i = 0; i <= n; i++) {
            dp[i][i] = 1;
            dp[i][1] = i;
            dp[i][0] = 1;
        }
        // 점화식으로 배열 완성하기(bottom-up)
        // i가 1인 경우는 초기화해놈
        for (int i = 2; i <= n; i++) {
            for (int j = 1; j < i; j++) {
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j];
            }
        }
        System.out.println(dp[n][k]);
    }
}