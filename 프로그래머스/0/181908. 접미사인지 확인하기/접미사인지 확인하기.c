#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* my_string, const char* is_suffix) {
    int answer = 0;
    int len= strlen(my_string);
    
    // 접미사 배열 저장
    char** suf_arr = (char**)malloc(sizeof(char*)*len);
    
    for(int i=0; i<len; i++){
        suf_arr[i]= strdup(my_string+i);
    }
    
    for(int j=0; j <len; j++){
        // if (is_suffix == suf_arr[j])
        // 문자열 일치하는 지 확인
        if(strcmp(is_suffix, suf_arr[j])==0){
            answer = 1;
        }
    }
    
    return answer;
}