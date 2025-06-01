#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, const char* overwrite_string, int s) {
    // 문자열 길이 구하기
    size_t len_ori = strlen(my_string);
    size_t len_copy = strlen(overwrite_string);
    // 문자열 저장 동적 할당
    char* answer = (char*)malloc(len_ori+1);
	
    // 원본 그대로 복사
    for(size_t i=0; i<(size_t)s; i++){
        answer[i] = my_string[i];
    }
    // 인덱스 s 부터 overwrite_string 복사
    for(size_t i=0; i<len_copy; i++){
        answer[s+i] = overwrite_string[i];
    }
    
    // 나머지 복사
    for(size_t i= s+len_copy; i<len_ori; i++){
        answer[i]=my_string[i];
    }
    // 널 문자 추가
    answer[len_ori]='\0';
    
    return answer;
}