
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int m = Integer.parseInt(br.readLine());

        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] a = new int[n];

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(a); // 배열 오름차순 정렬

        int cnt = 0; // 정답
        int s = 0; // 시작
        int e = n - 1; // 끝 인덱스

        while (s < e) { // 종료조건
            if (a[s] + a[e] > m) {
                e--;
            } else if (a[s] + a[e] < m) {
                s++;
            } else {
                cnt++;
                s++;
                e--;
            }
        }
        System.out.println(cnt);
    }
}
