

import java.io.*;
import java.util.Arrays;
import java.util.Scanner;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {

        // 빠른 입력
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        // 과목 개수: n
        int n = Integer.parseInt(br.readLine());

        // 점수 : int
        int[] score = new int[n];

        // 띄어쓰기로 구분
        StringTokenizer st = new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            score[i] = Integer.parseInt(st.nextToken());
        }
        br.close();
        Arrays.sort(score); // 정렬
        int max = score[n - 1];

        double avg = 0; // 평균
        for (int i = 0; i < n; i++) {
            avg += (double) score[i] / max * 100;
        }
        avg = avg / n;

        System.out.println(avg);
    }
}
