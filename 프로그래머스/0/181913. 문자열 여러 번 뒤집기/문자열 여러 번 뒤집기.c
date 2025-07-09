#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>
// queries_rows는 2차원 배열 queries의 행 길이, queries_cols는 2차원 배열 queries의 열 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_string, int** queries, size_t queries_rows, size_t queries_cols) {
    int len = strlen(my_string);

    char* answer = (char*)malloc(sizeof(char)*(len+1)); // null 포함
    strcpy(answer, my_string); // 문자열 복사
    
    
    for(int i=0; i<queries_rows; i++ ){
        int st = queries[i][0];
        int end = queries[i][1];
        while(st<end){
            char tmp = answer[st];
            answer[st]=answer[end];
            answer[end]=tmp;
            st++;
            end--;
        }
    }
    
    return answer;
}