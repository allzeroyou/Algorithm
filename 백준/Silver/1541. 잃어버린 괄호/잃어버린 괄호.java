
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        String temp = sc.nextLine();
        // -를 기준으로 나누기
        String[] arr = temp.split("-");

        // 정답
        int answer = 0;

        // 계산
        for (int i = 0; i < arr.length; i++) {
            int result = mySum(arr[i]); // string

            if (i == 0) { // 첫번째 요소는 더하기
                answer += result;
            } else {
                answer -= result;
            }
        }
        System.out.println(answer);
    }

    private static int mySum(String str) {
        int sum = 0;
        String[] strArr = str.split("[+]");
        for (int i = 0; i < strArr.length; i++) {
            sum += Integer.parseInt(strArr[i]);
        }
        return sum;
    }
}
