#include <string>
#include <vector>
#include <map>
#include <sstream>

using namespace std;

string solution(string letter) {
    string answer = "";
    // 모스부호 map
    map<string, char> morse = { 
        {".-", 'a'}, {"-...", 'b'}, {"-.-.", 'c'}, {"-..", 'd'}, {".", 'e'}, {"..-.", 'f'},
        {"--.", 'g'}, {"....", 'h'}, {"..", 'i'}, {".---", 'j'}, {"-.-", 'k'}, {".-..", 'l'},
        {"--", 'm'}, {"-.", 'n'}, {"---", 'o'}, {".--.", 'p'}, {"--.-", 'q'}, {".-.", 'r'},
        {"...", 's'}, {"-", 't'}, {"..-", 'u'}, {"...-", 'v'}, {".--", 'w'}, {"-..-", 'x'},
        {"-.--", 'y'}, {"--..", 'z'}
    };
    
    // 공백 단위로 문자열 분리
    stringstream ss(letter);
    string token;
    
    while(ss >> token){
        // 맵에서 해당 모스 부호 찾아 문자열에 추가
        if(morse.find(token)!=morse.end()){
            answer += morse[token];
        }
    }
    
    
    
    return answer;
}