
import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        // 벽돌의 개수
        int n = Integer.parseInt(br.readLine());

        // 1 based
        // arr[i] = {벽돌 번호, 밑면 넓이, 높이, 무게}

        int[][] arr = new int[n + 1][4];

        // 벽돌 정보 입력 받기
        for (int i = 1; i < n + 1; i++) {
            StringTokenizer st = new StringTokenizer(br.readLine());
            arr[i][0] = i;
            arr[i][1] = Integer.parseInt(st.nextToken()); // 밑면 넓이
            arr[i][2] = Integer.parseInt(st.nextToken()); // 높이
            arr[i][3] = Integer.parseInt(st.nextToken()); // 무게
        }


        // "무게" 기준으로 오름차순 정렬(가벼운 벽돌을 위에 쌓음)
        Arrays.sort(arr, new Comparator<int[]>() {
            @Override
            public int compare(int[] o1, int[] o2) {
                return Integer.compare(o1[3], o2[3]); // 무게 기준 정렬
            }
        });

        // 1. dp 테이블 생성
        // i번째 벽돌을 가장 아래에 두었을때 만드는 최대 높이
        int[] dp = new int[n + 1];

        // 2. 점화식
        // LIS(최장 증가 부분 수열)로 dp 테이블 갱신
        for (int i = 1; i < n + 1; i++) {
            for (int j = 0; j < i; j++) {
                // j번째 벽돌의 밑 넓이가 i번째 벽돌의 밑 넓이보다 작아야 위에 올림
                if (arr[i][1] > arr[j][1]) {
                    // j번째 벽돌을 아래에 두고, 벽돌을 추가한 높이 / 기존 높이 중 큰 값 선택
                    dp[i] = Math.max(dp[i], dp[j] + arr[i][2]);
                }
            }
        }

        // dp 배열 중 가장 높은 값 찾기(탑 최대 높이)
        int max_val = 0;
        for (int i : dp) {
            max_val = Math.max(i, max_val);
        }

        int idx = n;
        ArrayList<Integer> ans = new ArrayList<Integer>();

        while (idx != 0) {
            if (max_val == dp[idx]) { // 최대 높이 = 현재 벽돌 높이
                ans.add(arr[idx][0]); // 벽돌 번호
                max_val -= arr[idx][2]; // 현재 벽돌 높이만큼 줄이기
            }
            idx--;
        }

        // 사용된 벽돌 개수
        System.out.println(ans.size());

        // 사용된 벽돌 번호를 위->아래로 출력
        for (int i = ans.size() - 1; i >= 0; i--) {
            System.out.println(ans.get(i));
        }
    }
}
