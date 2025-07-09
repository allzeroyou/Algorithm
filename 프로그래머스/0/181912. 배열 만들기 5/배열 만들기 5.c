#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

// intStrs_len은 배열 intStrs의 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int* solution(const char* intStrs[], size_t intStrs_len, int k, int s, int l) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    int* answer = (int*)malloc(sizeof(int)*intStrs_len ) ;
    char dest[10000]; // 자른 문자열 저장
    // 실제 저장할 위치 인덱스
    int idx = 0;
    
    for(int i=0; i<intStrs_len; i++){
        // 문자열 자르기 ==> strncpy 함수 사용
        strncpy(dest, intStrs[i]+s, l); // s번 인덱스부터 l개 복사
        dest[l]='\0'; // 문자열 종료 문자 수동 추가
        printf("%s\n", dest);
        
        int num = atoi(dest);
        if( num > k){
            answer[idx++]=num;
        }
    }
    return answer;
}