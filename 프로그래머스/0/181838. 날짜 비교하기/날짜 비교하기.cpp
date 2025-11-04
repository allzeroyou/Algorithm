#include <string>
#include <vector>

using namespace std;

int solution(vector<int> date1, vector<int> date2) {
    int answer = 0;
    // 정수배열 date1, date2
    // 날짜가 앞서는거 -> year,month,day 모두 작거나 같아야 함.
    if(date1[0] < date2[0]){ // 1. 연도가 작을 경우
        return 1;
    }else if(date1[0] == date2[0]){ // 2. 연도가 같을 경우
        if(date1[1] < date2[1]){ // 3. 달이 작아야 빠른 날짜임
            return 1;
        }else if(date1[1]==date2[1]){ // 4. 달이 같을 경우
            if(date1[2] < date2[2]){ // 5. 날짜가 작아야 빠른 날짜임
                return 1;
            }
        }
    }
    return answer;
}