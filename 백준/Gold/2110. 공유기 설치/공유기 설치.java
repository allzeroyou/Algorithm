import java.io.*;
import java.util.*;

public class Main {
    static int[] home;
    static int n, c;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        n = Integer.parseInt(st.nextToken()); // 집
        c = Integer.parseInt(st.nextToken()); // 공유기 개수

        // 집의 좌표 저장
        home = new int[n];

        for (int i = 0; i < n; i++) {
            home[i] = Integer.parseInt(br.readLine());
        }

        // 가장 인접한 두 공유기 사이 최대 거리
        // 입력이 매우 크고, 수직선 위 집의 좌표이므로: 오름차순 정렬 필요 -> 이분탐색

        // 1. 오름차순 정렬
        Arrays.sort(home);

        // 2. 이분탐색 범위 변수 지정
        int low = 1; // 공유기 간 최소 거리의 최솟값
        int high = home[n - 1] - home[0];
        // 정답
        int ans = 0;

        while (low <= high) {
            int mid = (low + high) / 2;

            if (wifi(mid) < c) { // 최소거리가 mid 일때, 설치 가능한 공유기 개수 < 목표값 일때
                high = mid - 1;
            } else { // 아니라면, 최소거리가 가질 수 있는 최대거리 찾아낸다
                low = mid + 1;
                ans = mid;
            }
        }
        System.out.println(ans);
    }

    // 최소거리가 mid 일때 설치 가능한 공유기 개수
    private static int wifi(int dist) {
        int cnt = 1; // 첫번째 집은 무조건 설치
        int pre = home[0]; // 직전 위치 초기화

        for (int i = 1; i < n; i++) {
            int cur = home[i]; // 현재 위치
            if (cur - pre >= dist) { // 직전 위치와의 거리가 최소거리보다 클때
                // 공유기 설치 가능
                cnt++;
                pre = cur;
            }
        }
        return cnt;
    }
}
