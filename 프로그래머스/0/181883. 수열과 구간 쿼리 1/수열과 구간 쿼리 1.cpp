#include <string>
#include <vector>
#include <iostream>

using namespace std;

vector<int> solution(vector<int> arr, vector<vector<int>> queries) {
    vector<int> answer;
    // s이상 e이하인 i에 대해 +1
    for(int i=0; i<queries.size(); i++){
        int s=queries[i][0];
        int e=queries[i][1];
        
        for(int i=s; i<=e; i++){
            arr[i]+=1;
        }    
    }
    return arr;
}