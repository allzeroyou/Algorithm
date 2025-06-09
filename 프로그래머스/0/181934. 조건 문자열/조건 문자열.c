#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

// 파라미터로 주어지는 문자열은 const로 주어집니다. 변경하려면 문자열을 복사해서 사용하세요.
int solution(const char* ineq, const char* eq, int n, int m) {
    int answer = 0;
    
    // ineq: <, >
    // eq: =, ! 중 하나
    // 두 정수 n,m이 주어질때, n,m이 ineq, eq 조건에 맞으면 1/ 아님 0
    if(ineq[0]=='<'){
        if(eq[0]=='='){
            // n<= m
            if(n<=m) answer = 1;
        }else if(eq[0]=='!'){
            // n < m
            if(n<m) answer = 1;
        }
    }else if(ineq[0]=='>'){
        if(eq[0]=='='){
            // n>=m
            if(n>=m) answer = 1;
        }else if(eq[0]=='!'){
            // n>m
            if(n>m) answer = 1;
        }
    }
	// 여기까지 if 문에 안 걸렸다면 0    
    return answer;
}