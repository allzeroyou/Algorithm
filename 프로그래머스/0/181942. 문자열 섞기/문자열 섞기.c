#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* str1, const char* str2) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    
    size_t len = strlen(str1); // str1 == str2
    
    char* answer = (char*)malloc(len*2+1);
    
    for(size_t i =0; i<len; i++){
        answer[2*i]=str1[i]; // 번갈아 가면서 출력
        answer[2*i+1]=str2[i];
    }
    answer[len*2] = '\0'; // 문자열 마지막엔 null 추가
    
    return answer;
}