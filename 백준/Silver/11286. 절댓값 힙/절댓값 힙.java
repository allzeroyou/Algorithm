
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.PriorityQueue;

public class Main {
    public static void main(String[] args) throws IOException {
        // 시간 제한 1초 -> 시간복잡도 고려 해야 함
        // 우선순위큐 사용

        // 기준: 절댓값 최솟값, 절댓값이 같을 경우 음수 우선
        // 큐가 비어있을 경우: 0 출력

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        PriorityQueue<Integer> queue = new PriorityQueue<>((s1, s2) -> { // 기준 2개
            // 절댓값 작은 데이터 우선
            // 절댓값 같을 경우 음수 우선
            int firstStandard = Math.abs(s1);
            int secStardard = Math.abs(s2);
            if (firstStandard == secStardard) {
                return s1 > s2 ? 1 : -1; // 양수, 음수
            }

            return firstStandard - secStardard; // 참, 거짓으로 판단
        });
        for (int i = 0; i < n; i++) {
            int num = Integer.parseInt(br.readLine());
            if (num == 0) {
                if (queue.isEmpty()) {
                    System.out.println("0");
                } else {
                    System.out.println(queue.poll());
                }
            }else{
                queue.add(num);
            }
        }
    }
}
