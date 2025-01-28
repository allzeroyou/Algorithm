import java.io.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 2xn 크기
        int n = Integer.parseInt(br.readLine());

        // 1. dp 테이블 설정
        int[] dp = new int[n + 1];

        // 3. 초기값 설정
        // 1인 경우 예외처리 해준다!
        if (n == 1) {
            dp[1] = 1;
            System.out.println(dp[n]);
            return;
        }

        dp[1] = 1;
        dp[2] = 2;

        // 2. 점화식 도출
        // int overflow가 발생하지 않도록 결과 반환시에만 10007을 나눠주는 것이 아닌 계산마다 나눈 값을 저장해야 한다!
        for (int i = 3; i <= n; i++) {
            dp[i] = (dp[i - 2] + dp[i - 1]) % 10007;
        }

        // 답 도출
        System.out.println(dp[n]);
    }
}
