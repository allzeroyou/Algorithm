import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine()); // 공백 기준으로 나누기

        int n = Integer.parseInt(st.nextToken()); // 심사대
        int m = Integer.parseInt(st.nextToken()); // 사람

        // 입국심사 시간 배열
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(br.readLine());
        }

        // 이분 탐색
        Arrays.sort(arr);
        long low = 1;
        long high = (long) m * arr[n - 1]; // 10억 * 10억 -> int형 표현 범위(21억) 벗어나기 때문에 -> long형 사용
        long ans = high; // 정답: 최소 시간 저장

        while (low <= high) {
            long mid = (low + high) / 2;

            long people = 0; // 현재 시간(mid)동안 처리할 수 있는 사람 수

            for (int time : arr) {
                people += mid / time;
                if (people >= m) break; // 이미 필요한 사람 수를 초과할때 더 계산할 필요 없음
            }

            if (people >= m) {
                ans = mid; // 가능한 경우 최솟값 갱신
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        System.out.println(ans);
    }
}
