#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* myString) {
    // 문자열 길이
    size_t len = strlen(myString); // strlen() -> size_t 반환
    
    // 동적할당  
    char* answer = (char*)malloc(len+1);
    
    // 소문자 => 대문자 변환
    for(int i=0; i<len; i++){
        char c = myString[i];
        // a~z -> 아스키코드 : 97~122 사이에 있다면 -32 해서 대문자로 변경(A: 65)
        if (c>='a' && c<= 'z'){
            answer[i]= c - 32;
        }
        else {
            answer[i] = c; 
        }
    }
    // 문자열 맨 마지막은 null
    answer[len]='\0';
    
    return answer;
}