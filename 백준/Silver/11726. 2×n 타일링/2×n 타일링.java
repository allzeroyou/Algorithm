
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        long dp[] = new long[1001];
        // dp 테이블 초기화
        dp[1] = 1; // n=1 일때 타일 채우는 경우의 수
        dp[2] = 2; // n=2 일때 타일 채우는 경우의수
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i - 1] + dp[i - 2]) % 10007; // 할때마다 나누는거랑 맨 마지막에 나누는거랑 결과 같음.
        }
        System.out.println(dp[n]);
    }
}
