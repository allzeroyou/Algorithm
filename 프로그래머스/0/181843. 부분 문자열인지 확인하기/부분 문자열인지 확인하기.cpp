#include <string>
#include <vector>

using namespace std;

int solution(string my_string, string target) {
    int answer = 0;
    // my_string에 target이 부분문자열로 존재하는지?
    // find의 반환값은 size_t == 부호없는정수임(항상 >=0)
    if(my_string.find(target)!=string::npos){
        return 1;
    }else{
        return 0;
    }
}