import java.io.*;
import java.util.*;

public class Main {

    public static void main(String[] args) throws IOException {
        // 0. 입력 및 초기화
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 테스트케이스 개수
        int n = Integer.parseInt(br.readLine());

        // 1. dp 테이블 정의
        HashMap<Integer, int[]> dp = new HashMap<>();

        // 3. 초깃값 설정
        dp.put(0, new int[]{1, 0});
        dp.put(1, new int[]{0, 1});

        // 2. 점화식 도출
        // f(n)일때 0과 1의 개수= f(n-2)의 0과 1의 개수 + f(n-1)의 0과 1의 개수
        for (int i = 2; i <= 40; i++) {
            int[] pre1 = dp.get(i - 1);
            int[] pre2 = dp.get(i - 2);
            dp.put(i, new int[]{pre1[0] + pre2[0], pre1[1] + pre2[1]});
        }

        // 테스트 케이스
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            int[] tmp = dp.get(num);

            System.out.println(tmp[0] + " " + tmp[1]);
        }
    }
}
