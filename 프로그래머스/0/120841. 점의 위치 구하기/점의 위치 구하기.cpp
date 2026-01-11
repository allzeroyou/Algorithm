#include <string>
#include <vector>

using namespace std;

int solution(vector<int> dot) {
    int answer = 0;
    // 사분면 알아내기
    if(dot[0]>0 && dot[1]>0)
    {
        return 1;
    }else if(dot[0]>0 && dot[1]<0){
        return 4;
    }else if(dot[0]<0 && dot[1]>0){
        return 2;
    }else{
        return 3;
    }
}