#include <string>
#include <vector>
#include <numeric>

using namespace std;

vector<int> solution(int numer1, int denom1, int numer2, int denom2) {
    vector<int> answer;
    int result = lcm(denom1, denom2);
    
    // 곱해야하는 수
    int mul1 = result/denom1;
    int mul2 = result/denom2;
    
    int bunza = numer1*mul1 + numer2*mul2;
    int bunmo = result;
    
    // 기약분수로 변환
    int com_div = gcd(bunza, bunmo);
    
    bunza /= com_div;
    bunmo /= com_div;
    
    answer.push_back(bunza);
    answer.push_back(bunmo);
    
    return answer;
}