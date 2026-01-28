#include <string>
#include <vector>
#include <sstream>

using namespace std;

int solution(string s) {
    int answer = 0;
    int last_num = 0;
    
    stringstream ss(s);
    string word;
    
    while(ss >> word){
        if(word == "Z"){
            answer -= last_num;
        }else{
            last_num = stoi(word);
            answer += last_num;
        }
    }
    return answer;
}