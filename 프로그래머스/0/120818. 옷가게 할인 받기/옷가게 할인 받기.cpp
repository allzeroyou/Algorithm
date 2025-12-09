#include <string>
#include <vector>

using namespace std;

int solution(int price) {
    int answer = 0;
    if(price>=500000){
        answer = price*(1-0.2);
        return answer;
    }if(price>=300000){
        answer = price*(1-0.1);
        return answer;
    }
    if(price>=100000){
        answer = price*(1-0.05);
        return answer;
    }
    return price;
}