#include <string>
#include <vector>

using namespace std;

vector<vector<int>> solution(vector<vector<int>> arr) {
    vector<vector<int>> answer;

    if(arr[0].size() > arr.size()){ // 열 > 행
        for(int i=arr.size(); i<arr[0].size(); i++){
            arr.push_back(vector<int>(arr[0].size(), 0)); // 열 개수 만큼 0 채움
        }
        return arr;
    }else if(arr[0].size() < arr.size()){ // 열 < 행
        int diff = arr.size()-arr[0].size(); // 부족한 열 개수
        for(int i=0; i<arr.size(); i++){
            // 행마다 diff 개수만큼 뒤에 붙이기
            arr[i].insert(arr[i].end(), diff, 0);
        }
        return arr;
    }else{
        return arr;
    }
}