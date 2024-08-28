
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String str = sc.next();

        int arr[] = new int[str.length()];

        for (int i = 0; i < str.length(); i++) {
            arr[i] = Integer.parseInt(str.substring(i, i + 1)); // 자릿수로 잘라서 배열에 저장
            // substring(startIdx, endIdx): 시작은 포함, 끝은 미포함
        }
        // 선택정렬
        for (int i = 0; i < str.length(); i++) {
            int max = i;
            for (int j = i; j < str.length(); j++) {
                if (arr[j] > arr[max]) { // 최댓값 보다 크다면
                    max = j;
                }
            }
            if (arr[i] < arr[max]) {
                int temp = arr[i];
                arr[i] = arr[max];
                arr[max] = temp;
            }
        }
        for (int i = 0; i < str.length(); i++) {
            System.out.print(arr[i]);
        }
    }
}

