#include <string>
#include <vector>

using namespace std;

int solution(int n) {
    int answer = 0;
    int fac = 1;
    int i = 1;
    
    while(true){
        fac *= i;
        if(fac>n){
            answer = i-1;
            break;
        }else if(fac==n){
            answer = i;
            break;
        }
        i++;
    }
    
    return answer;
}