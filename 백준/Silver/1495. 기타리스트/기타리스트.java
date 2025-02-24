
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        String NSM = br.readLine();
        StringTokenizer st = new StringTokenizer(NSM, " ");
        int N = Integer.parseInt(st.nextToken());
        int S = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // 각 곡마다 조절할 수 있는 볼륨 변화량
        String str = br.readLine();
        st = new StringTokenizer(str, " ");

        int[] arr = new int[N + 1];
        for (int i = 1; i <= N; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        // 1. dp 테이블
        int[] dp = new int[M + 1]; // 특정 볼륨이 몇 번째 곡에서 가능한지를 저장
        Arrays.fill(dp, -1); // // 모든 볼륨을 초기에는 불가능 상태(-1)
        dp[S] = 0;  // 시작 볼륨 S는 0번째 곡에서 가능

        int ans = -1; // 최댓값 저장

        for (int n = 1; n <= N; n++) {
            List<Integer> change = new ArrayList<>(); // 현재 곡에서 가능한 볼륨 목록

            // 이전 곡(n-1)에서 나올 수 있는 볼륨
            for (int m = 0; m <= M; m++) {
                if (dp[m] == n - 1) { // 이전 곡에서 가능했던 볼륨이라면
                    int plus = m + arr[n];
                    int minus = m - arr[n];
                    
                    // 범위 이내라면 추가
                    if (plus <= M) change.add(plus);
                    if (minus >= 0) change.add(minus);
                }
            }

            for (int i = 0; i < change.size(); i++) {
                int change_idx = change.get(i);
                dp[change_idx] = n; // 현재 곡에서 이 볼륨이 가능한지 표시
                
                // 마지막 곡이라면 최댓값 갱신
                if (n == N) ans = Math.max(ans, change_idx);
            }
        }
        // 결과 출력
        System.out.println(ans);
    }
}
