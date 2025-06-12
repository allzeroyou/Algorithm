#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int solution(int a, int b, int c) {
    int answer = 0;
    
    if(a!=b && a!=c && b!=c){
        answer = a+b+c;
    }else if((b==c)&& (b!=a) || (a==c)&& (b!=a) || (a==b)&& (b!=c)){
        answer = (a+b+c)*(a*a+b*b+c*c);
    }else {
        answer = (a+b+c)*(a*a+b*b+c*c)*(a*a*a +b*b*b +c*c*c);
    }
    
    return answer;
}