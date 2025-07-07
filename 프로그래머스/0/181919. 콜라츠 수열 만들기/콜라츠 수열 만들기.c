#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int* solution(int n) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*n);
    answer[0]=n;
    int tmp = n;
    
    for(int i=1; i<n; i++){
        if(tmp % 2==0){
            tmp = tmp/2;
            answer[i]= tmp;
        }
        else
        {
            tmp = 3*tmp +1;  
            answer[i]=tmp;
        }
    }
    
    return answer;
}