
import java.util.LinkedList;
import java.util.Queue;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();

        // 카드 배열 생성 -> 큐 사용
        // 앞에서 제거(dequeue), 뒤에 추가(enqueue) 연산 효율적(n이 최대 50만임)
        Queue<Integer> card = new LinkedList<>();

        for (int i = 1; i <= n; i++) {
            card.add(i);
        }

        // 로직 실행
        while (card.size() > 1) { // 한장 남을때까지
            card.poll(); // 제일 위 카드 버리기
            // 그 다음 카드를 제일 아래로 옮기기
            card.add(card.poll());
        }
        // 마지막 남은 카드 출력
        System.out.println(card.poll());

        sc.close();
    }
}
