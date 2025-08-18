#include <string>
#include <vector>

using namespace std;

int solution(vector<int> num_list) {
    int answer = 0;
    
    // 정수리스트 num_list
    // 가장 첫번째 원소: 1번 원소
    // 홀수, 짝수 번째 원소들 중 가장 큰 값 return
    // 두 값이 같을 경우 그 값 return
    int even = 0; // 짝수
    int odd = 0; // 홀수
    
    for(int i=1; i<num_list.size()+1; i++){
        if(i%2== 0){
            even += num_list[i-1];
        }else{
            odd += num_list[i-1];
        }
    }
    printf("%d, %d", odd, even);
    
    return answer = (even>=odd)? even:odd;
}