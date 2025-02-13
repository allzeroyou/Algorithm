import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        // 0. 입력 및 초기화
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // n개의 정수 수열
        int n = Integer.parseInt(br.readLine());

        // 수열 관리
        int[] seq = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            seq[i] = Integer.parseInt(st.nextToken());
        }

        // 1. dp 테이블 정의
        int[] dp = new int[n];

        // 3. 초기값 설정
        dp[0] = seq[0];
        int maxSum = dp[0]; // 최댓값 초기화

        // 2. 점화식 도출
        for (int i = 1; i < n; i++) {
            dp[i] = Math.max(dp[i - 1] + seq[i], seq[i]); // 누적합, 현재 수열 원소 중 큰 값을 저장한다
            maxSum = Math.max(maxSum, dp[i]);
        }

        System.out.println(maxSum);
    }
}
