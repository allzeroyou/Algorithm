#include <string>
#include <vector>
#include <algorithm> // find 함수 사용

using namespace std;

vector<int> solution(vector<int> arr, vector<int> delete_list) {
    vector<int> answer;
    // arr 원소 중 delete_list 원소를 모두 삭제,남은 원소들은 유지
    // find 함수 사용
    for(int num: arr){
        // delete_list에 포함되지 않은 원소만 추가
        if(find(delete_list.begin(), delete_list.end(), num)==delete_list.end()){
            answer.push_back(num);
        }
    }

    return answer;
}