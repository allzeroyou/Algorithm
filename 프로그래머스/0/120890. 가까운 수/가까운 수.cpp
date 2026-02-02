#include <string>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

int solution(vector<int> array, int n) {
    sort(array.begin(), array.end());
    
    int answer = array[0];
    int minDiff = abs(array[0]-n);
    
    for(int i=1; i<array.size(); i++){
        int curDiff = abs(array[i]-n);
        if(curDiff < minDiff){
            minDiff = curDiff;
            answer = array[i];
        }
    }
    return answer;
}