#include <string>
#include <vector>

using namespace std;

int solution(int slice, int n) {
    int answer = 0;
    // 2~10 조각으로 잘라줌
    // 1조각 이상씩 먹어야 함
    if(n%slice!=0){
        answer = n/slice + 1;
    }else{
        answer = n/slice;
    }
    return answer;
}