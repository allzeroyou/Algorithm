#include <stdio.h>

int main(void) {
    int a;
    scanf("%d", &a);

    if(a%2 != 0){
        printf("%d is odd\n", a);
    }else{
        printf("%d is even\n", a);
    }
    return 0;
}