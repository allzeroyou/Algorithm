import java.io.*;
import java.util.*;

public class Main {
    static int[] a;
    static int[] b;
    static int n, m;

    static int biSearch(int target) {
        int st = 0;
        int en = n - 1;

        while (st <= en) { // 이분 탐색 종료 조건: 해당 값이 배열에 없을 경우 -> st, en이 역전됨.
            int mid = (st + en) / 2;

            if (a[mid] < target) st = mid + 1;
            else if (a[mid] > target) en = mid - 1;
            else return 1; // 찾은 경우 1 반환 후 종료
        }
        // st > en 일 경우 배열에 없음!
        return 0;
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        n = Integer.parseInt(br.readLine()); // 배열 요소 개수

        // 배열 a
        a = new int[n];
        StringTokenizer st = new StringTokenizer(br.readLine());

        for (int i = 0; i < n; i++) {
            a[i] = Integer.parseInt(st.nextToken());
        }

        m = Integer.parseInt(br.readLine()); // 찾으려는 숫자 개수
        // 배열 b
        b = new int[m];
        st = new StringTokenizer(br.readLine());
        for (int i = 0; i < m; i++) {
            b[i] = Integer.parseInt(st.nextToken());
        }

        // 이분탐색 로직 구현
        // 배열-오름차순 정렬
        Arrays.sort(a);

        for (int i = 0; i < m; i++) {
            int ans = biSearch(b[i]);
            System.out.println(ans);
        }
    }
}