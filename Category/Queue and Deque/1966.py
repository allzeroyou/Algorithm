'''
1. 테스트케이스 수 입력
2. 문서의 개수, 인쇄되었는지 궁금한 문서가 현재 큐에서 몇 번째에 놓여있는지 나타내는 정수
3.

'''

from collections import deque
import sys

test_case = int(input())

for _ in range(test_case):
    n, m =map(int, input().split())
    print_list = list(map(int, input().split()))
    check_list = [0 for _ in range(n)]
    check_list[m]=1

    count = 0
    while True:
        if print_list[0]==max(print_list):
            count += 1
            if check_list[0]==max(print_list):
                count += 1

                if check_list[0] != 1:
                    del print_list[0]
                    del check_list[0]
                else:
                    print(count)
                    break
        else:
            print_list.append(print_list[0])
            check_list.append(check_list[0])
            del print_list[0]
            del check_list[0]