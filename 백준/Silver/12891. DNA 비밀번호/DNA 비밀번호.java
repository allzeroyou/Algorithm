
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    // 전역변수화
    static int curArr[];
    static int checkArr[];
    static int cnt;

    public static void main(String[] args) throws IOException {
        // 슬라이딩 윈도우: 고정된 범위를 정해 탐색(vs 투포인터: 범위 유동적)
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int s = Integer.parseInt(st.nextToken());
        int p = Integer.parseInt(st.nextToken());

        // 정답
        int ans = 0;

        // 구해야할 dna 순서 입력받음
        checkArr = new int[4];
        // 현재 상태 배열
        curArr = new int[4];

        // 입력받은 문자열
        char arr[] = new char[s];

        // dna 일치 개수(4가 되어야 함)
        cnt = 0;

        arr = br.readLine().toCharArray();
        st = new StringTokenizer(br.readLine());

        for (int i = 0; i < 4; i++) {
            checkArr[i] = Integer.parseInt(st.nextToken());
            if (checkArr[i] == 0) { // 4가 만족되는 수인데, 0은 이미 만족되는 수임
                cnt++;
            }
        }
        for (int i = 0; i < p; i++) { // 부분문자열 처음 받을때 세팅
            Add(arr[i]);
        }
        if (cnt == 4) {
            ans++;
        }
        // 슬라이딩윈도우
        for (int i = p; i < s; i++) {
            int j = i - p;
            Add(arr[i]);
            Remove(arr[j]);
            if (cnt == 4) ans++;
        }
        System.out.println(ans);
        br.close();
    }

    private static void Add(char c) {
        switch (c) {
            case 'A':
                curArr[0]++;
                if (curArr[0] == checkArr[0]) cnt++;
                break;
            case 'C':
                curArr[1]++;
                if (curArr[1] == checkArr[1]) cnt++;
                break;
            case 'G':
                curArr[2]++;
                if (curArr[2] == checkArr[2]) cnt++;
                break;
            case 'T':
                curArr[3]++;
                if (curArr[3] == checkArr[3]) cnt++;
                break;
        }
    }

    private static void Remove(char c) {
        switch (c) {
            case 'A':
                if (curArr[0] == checkArr[0]) cnt--;
                curArr[0]--;
                break;
            case 'C':
                if (curArr[1] == checkArr[1]) cnt--;
                curArr[1]--;
                break;
            case 'G':
                if (curArr[2] == checkArr[2]) cnt--;
                curArr[2]--;
                break;
            case 'T':
                if (curArr[3] == checkArr[3]) cnt--;
                curArr[3]--;
                break;
        }
    }
}
