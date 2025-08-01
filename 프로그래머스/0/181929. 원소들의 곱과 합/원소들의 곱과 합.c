#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len) {
    int answer = 0;
    
    // 모든 원소 곱 < 모든 원소 합 -> 1 return
    int multiple = 1;
    int plus = 0;
    
    for(int i=0; i< num_list_len; i++){
        plus += num_list[i];
        multiple *= num_list[i];
    }
    
    if(multiple<(plus*plus)){
        answer = 1;
    }else{
        answer = 0;
    }
    
    return answer;
}