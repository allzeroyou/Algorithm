#include <string>
#include <vector>
#include <iostream>

using namespace std;

string solution(int q, int r, string code) {
    string answer = "";
    int len = code.length();
    
    for(int i=0; i<len; i++){        
        if(i % q == r){
            answer+= code[i];
        }
    }
    
    return answer;
}