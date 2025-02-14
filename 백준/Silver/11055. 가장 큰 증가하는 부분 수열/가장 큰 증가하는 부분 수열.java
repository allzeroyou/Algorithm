import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        // 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        // 수열
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        // dp 테이블
        int[] dp = new int[n];

        // 초기값
        dp[0] = a[0];

        // 최댓값
        int maxSum = a[0];

        if(n==1){
            System.out.println(maxSum);
            return;
        }

        // 점화식
        // "증가하는" 부분수열 중 합이 가장 큰 것 -> 증가하는 걸 체크하기 위한 j 이터레이터를 하나 더 둔다
        for (int i = 1; i < n; i++) {
            dp[i] = a[i]; // 현재 요소를 dp 테이블에 저장
            for (int j = 0; j < i; j++) {
                if (a[j] < a[i]) { // 증가하는 부분 수열인지 검증
                    dp[i] = Math.max(dp[i], dp[j] + a[i]);
                }
            }
            // 최댓값 반환
            maxSum = Math.max(maxSum, dp[i]);
        }
        System.out.println(maxSum);
    }
}
