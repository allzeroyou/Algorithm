#include <string>
#include <vector>
#include <sstream>
#include <iostream>

using namespace std;

int solution(string binomial) {
    int answer = 0;
    // 문자열: a op b 형식
    // a,b 계산 
    // 문자열 -> 배열로 만들고, a:0번째, op: 2번째, b: 4번째
    istringstream iss(binomial);
    string token;
    string arr[10];
    int idx = 0;
    
    while(iss >> token){
        arr[idx++]=token;
    }
    
    for(int i=0; i<idx; i++){
        cout<< arr[i]<< " ";
    }
    
    // 숫자로 변환 -> 공백은 제거
    int n1 = stoi(arr[0]);
    int n2 = stoi(arr[2]);
    
    // 2번째 요소를 연산자로
    char op = arr[1][0];
    
    switch(op){
        case '+': answer = n1+n2; break;
        case '-': answer = n1-n2; break;
        case '*': answer = n1*n2; break;       
    }
    
    return answer;
}