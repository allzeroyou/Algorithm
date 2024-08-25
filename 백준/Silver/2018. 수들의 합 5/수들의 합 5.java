

import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int cnt = 1;
        int st_idx = 1;
        int ed_idx = 1;
        int sum = 1;
        while(ed_idx!=n){
            if(sum==n){
                cnt++;
                ed_idx++;
                sum = sum + ed_idx;
            } else if(sum>n){
                sum = sum - st_idx;
                st_idx ++;
            } else{
                ed_idx++;
                sum = sum + ed_idx;
            }
        }
        System.out.println(cnt);
    }
}
