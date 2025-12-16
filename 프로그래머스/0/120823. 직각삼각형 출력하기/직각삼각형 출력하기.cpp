#include <iostream>

using namespace std;

int main(void) {
    int n;
    cin >> n;
    for(int i=1; i<=n; i++){
        for(int j=0; j<i; j++){ // 별 찍는용
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}