
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 띄어쓰기 구분
        StringTokenizer st = new StringTokenizer(br.readLine());
        // n: 개수, m: 합을 구해야 하는 횟수
        int n = Integer.parseInt(st.nextToken());
        int m = Integer.parseInt(st.nextToken());
        // 숫자 배열
        long[] arr = new long[n];
        // 합 배열
        long[] sum_arr = new long[n + 1];

        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
            sum_arr[i + 1] = sum_arr[i] + arr[i];
        }
        for (int i = 0; i < m; i++) {
            st = new StringTokenizer(br.readLine());
            int s = Integer.parseInt(st.nextToken());
            int e = Integer.parseInt(st.nextToken());
            // 구간합 공식
            System.out.println(sum_arr[e] - sum_arr[s - 1]);
        }
    }
}
