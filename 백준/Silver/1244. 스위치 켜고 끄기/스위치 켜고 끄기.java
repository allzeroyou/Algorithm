import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        int[] arr = new int[n + 1];

        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 1; i <= n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int cnt = Integer.parseInt(br.readLine());


        for (int i = 0; i < cnt; i++) {
            st = new StringTokenizer(br.readLine());

            int gen = Integer.parseInt(st.nextToken());
            int num = Integer.parseInt(st.nextToken());

            if (gen == 1) { // 남자
                for (int k = num; k <= n; k += num) {
                    if (arr[k] == 1) {
                        arr[k] = 0;
                    } else {
                        arr[k] = 1;
                    }
                }
            } else { // 여자
                int left = num - 1;
                int right = num + 1;
                while (left > 0 && right <= n) {
                    if (arr[left] != arr[right]) {
                        break;
                    }
                    left--;
                    right++;
                }
                for (int k = left + 1; k < right; k++) {
                    if (arr[k] == 1) {
                        arr[k] = 0;
                    } else {
                        arr[k] = 1;
                    }
                }
            }
        }
        // 출력
        StringBuilder sb = new StringBuilder();
        for (int i = 1; i <= n; i++) {
            sb.append(arr[i]).append(" ");
            if (i % 20 == 0) {
                sb.append("\n");
            }
        }
        System.out.println(sb);
    }
}
