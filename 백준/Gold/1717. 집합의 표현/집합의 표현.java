
import java.util.Scanner;

public class Main {
    static int parent[];

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int m = sc.nextInt();
        // parent
        parent = new int[n + 1];
        // 대표노드 -> 자기 자신으로 초기화
        for (int i = 0; i < n + 1; i++) {
            parent[i] = i; // 초기엔 각 노드가 자신을 부모로 가짐
        }
        for (int i = 0; i < m; i++) { // 계산
            int question = sc.nextInt();
            int a = sc.nextInt();
            int b = sc.nextInt();
            if (question == 0) { // union
                union(a, b);
            } else {
                boolean res = checkSame(a, b);
                if (res) {
                    System.out.println("YES");
                } else {
                    System.out.println("NO");
                }
            }
        }
    }

    private static void union(int a, int b) {
        // 대표 노드 찾아서 연결
        a = find(a);
        b = find(b);
        if (a != b) {
            parent[b] = a; // 두개 연결하겠음
        }
    }

    private static int find(int a) {
        if (a == parent[a]) { // 대표노드 일때
            return a;
        } else {
            return parent[a] = find(parent[a]); // value를 index로 바꿔서 재귀 again && parent 업데이트
        }
    }

    private static boolean checkSame(int a, int b) {
        a = find(a);
        b = find(b);
        if (a == b) return true;
        else return false;
    }
}
