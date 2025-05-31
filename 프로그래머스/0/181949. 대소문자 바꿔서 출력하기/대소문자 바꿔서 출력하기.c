#include <stdio.h>
#define LEN_INPUT 10
#include <string.h>
#include <stdlib.h> // malloc 선언

int main(void) {
    char s1[LEN_INPUT];
    scanf("%s", s1);
    
	size_t len = strlen(s1);
    // 문자열 배열
    char* answer = (char*)malloc(len+1);
    
    // 소문자 -> 대문자 & 대문자 -> 소문자로 변환
    for(size_t i=0; i<len; i++){
        char c = s1[i];
        
        if(c>='a' && c<= 'z')
        {
        	answer[i] = c - 32;   
        }
        else
        {
        	answer[i] = c + 32;    
        }
    }
    // 마지막에 null 종료 문자를 붙여야 printf 시 정상 출력
    answer[len] = '\0';
    
    printf("%s\n", answer);
    
    // 동적 할당 해제
    free(answer);
    
    return 0;
}
