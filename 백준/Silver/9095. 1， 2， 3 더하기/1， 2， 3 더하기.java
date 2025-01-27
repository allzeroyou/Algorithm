import java.io.*;

public class Main {
    public static void main(String args[]) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // test case
        int tc = Integer.parseInt(br.readLine());


        for(int i=0; i<tc; i++){
            int n = Integer.parseInt(br.readLine());

            // 1. 테이블 정의
            int[] dp = new int[11]; // n은 11보다 작음

            // 3. 초기값 설정
            dp[1]=1;
            dp[2]=2;
            dp[3]=4;

            // 2. 점화식 도출
            for(int k=4; k<=n; k++){
                dp[k]=dp[k-1]+dp[k-2]+dp[k-3];
            }

            System.out.println(dp[n]);
        }

    }
}
