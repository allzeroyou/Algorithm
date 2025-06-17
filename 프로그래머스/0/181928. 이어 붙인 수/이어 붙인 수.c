#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// num_list_len은 배열 num_list의 길이입니다.
int solution(int num_list[], size_t num_list_len) {
    int answer = 0;
    
    char odd_str[100] = "";
    char even_str[100] = "";
    char tmp[2]; // 임시 문자열
    
    for(int i=0; i<num_list_len; i++){
        sprintf(tmp, "%d", num_list[i]); // 정수 -> 문자열로 변환.
        
        if(num_list[i]%2 != 0 ){    
            // 홀수
            strcat(odd_str, tmp);
        }else{
            // 짝수
            strcat(even_str, tmp);
        }
    }
    
    // 문자열 -> 정수 변환
    int odd_num = atoi(odd_str);
    int even_num = atoi(even_str);
    
    
    return odd_num + even_num;
    
    
}