#include <string>
#include <vector>

using namespace std;

int solution(vector<int> box, int n) {
    int answer = 1;
    // 가로, 세로, 높이 배열 저장된 box
    // 주사위 모서리 길이 -> 상자에 들어갈 수 있는 주사위 최대개수?
    answer= (box[0]/n) * (box[1]/n) * (box[2]/n);
    return answer;
}