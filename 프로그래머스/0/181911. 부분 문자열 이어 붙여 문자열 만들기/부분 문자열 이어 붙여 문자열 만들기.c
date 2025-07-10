#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// my_strings_len은 배열 my_strings의 길이입니다.
// parts_rows는 2차원 배열 parts의 행 길이, parts_cols는 2차원 배열 parts의 열 길이입니다.
// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
char* solution(const char* my_strings[], size_t my_strings_len, int** parts, size_t parts_rows, size_t parts_cols) {
    // return 값은 malloc 등 동적 할당을 사용해주세요. 할당 길이는 상황에 맞게 변경해주세요.
    char* answer = (char*)malloc(100+1);
    answer[0] = '\0'; // 문자열 초기화 -> strcat 용
    
    for(int i =0; i<parts_rows; i++){
        char* tmp = (char*)malloc(100+1);
        int st = parts[i][0];
        int end = parts[i][1];
        int len = end - st +1;
        
        strncpy(tmp, my_strings[i]+st, len);
        tmp[len]='\0';
        strcat(answer, tmp);
        
    }
    
    return answer;
}