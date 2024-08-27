
import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        // 1~n까지 수
        int n = Integer.parseInt(sc.nextLine());
        // 만들 수열
        int[] suyeol = new int[n];
        for (int i = 0; i < n; i++) {
            suyeol[i] = sc.nextInt();
        }
        // 1~n 까지 수와 수열 비교해 스택 push/pop 결정
        // 스택
        Stack<Integer> stack = new Stack<>();

        // 연산 과정을 저장할 string builder
        StringBuilder sb = new StringBuilder();

        // 스택에 넣을 수, 자연수 1부터 시작
        int num = 1;
        boolean flag = true; // 수열 생성 가능 여부

        for (int i = 0; i < n; i++) {
            int cur = suyeol[i]; // 현재 만들어야 할 수
            // 현재 수보다 작거나 같은 수까지 스택에 push
            while (num <= cur) {
                stack.push(num); //
                sb.append("+\n");
                num++;
            }
            // 스택이 비어있거나 top이 현재 수와 다를 경우 수열 생성 불가
            if (stack.isEmpty() || stack.peek() != cur) {
                flag = false;
                break;
            }

            stack.pop(); // 현재 수를 꺼냄
            sb.append("-\n");
        }
        // 결과 출력
        if (flag) {
            System.out.println(sb);
        } else {
            System.out.println("NO");
        }
        sc.close();
    }
}
