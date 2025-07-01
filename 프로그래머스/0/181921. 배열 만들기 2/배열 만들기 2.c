#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

int* solution(int l, int r) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(1000000);
    char tmp[1000000];
    int cnt =0;

    for(int i=l; i<=r; i++){
        if(i%5==0){ // 일단 5의 배수만 바꾸자
            sprintf(tmp, "%d", i);
            int len = strlen(tmp);
            int valid = 1; // 유효성 flag

            for(int j=0; j<len; j++){
                if(tmp[j]!='5' && tmp[j]!='0'){
                    valid = 0;
                    break;
                }
            }
            if(valid){
                answer[cnt++]=i;
            }
        }
    }
    if(cnt == 0){
        answer[0]=-1;
        cnt =1;
    }
    
    return answer;
}