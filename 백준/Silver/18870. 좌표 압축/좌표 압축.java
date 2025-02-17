import java.io.*;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        // 원소 배열
        int[] arr = new int[n];

        String line = br.readLine(); // 두 번째 줄 전체 읽기
        StringTokenizer st = new StringTokenizer(line); // 공백 기준으로 나누기

        for (int i = 0; i < n; i++) {
            arr[i] = Integer.parseInt(st.nextToken());
        }
        //System.out.println(Arrays.toString(arr));

        // 0. set 배열 만들기
        Set<Integer> number = new HashSet<>();
        for (int num : arr) {
            number.add(num); // 배열을 set에 추가
        }

        // 1. 집합의 요소를 오름차순 정렬한다.
        List<Integer> sortedKey = new ArrayList<>(number);
        Collections.sort(sortedKey);

        // 2. 등수 매기기
        int rank = 0;
        HashMap<Integer, Integer> rankMap = new HashMap<>();

        for (int key : sortedKey) {
            rankMap.put(key, rank++); // 순위 증가
        }

        // 4. 입력받은 원소 배열을 순회하면서 hashmap에서 value(등수) 출력
        StringBuilder sb = new StringBuilder();
        for (int num : arr) {
            sb.append(rankMap.get(num)).append(" ");
        }
        System.out.println(sb.toString().trim());
    }
}
