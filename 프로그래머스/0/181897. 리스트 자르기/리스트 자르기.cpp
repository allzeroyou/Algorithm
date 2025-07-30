#include <string>
#include <vector>

using namespace std;

vector<int> solution(int n, vector<int> slicer, vector<int> num_list) {
    vector<int> answer;
    // slicer 배열 순서: a,b,c
    int st, end, step;
    
    // 기본 step  =1
    step = 1;
    
    // case별 st, end, step 설정
    switch(n){
        case 1:
            st = 0;
            end = slicer[1];
            break;
        case 2:
            // n=2 일때 num_list의 a번 인덱스부터 마지막 인덱스까지
            st = slicer[0];
            end = num_list.size()-1;
            break;
        case 3:
            // n=3 일때 num_list의 a번 인덱스부터 b번 인덱스까지
            st = slicer[0];
            end = slicer[1];
            break;
        case 4:
            // n=4 일때 num_list의 a번 인덱스부터 b번 인덱스까지 c간격으로
            st = slicer[0];
            end = slicer[1];
            step = slicer[2];
            break;
    }
    // 슬라이싱
    for(int i=st; i<=end; i+=step){
        answer.push_back(num_list[i]);
    }
    
    
    return answer;
}