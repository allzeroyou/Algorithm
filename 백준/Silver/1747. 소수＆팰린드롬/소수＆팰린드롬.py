import math
import sys

input = sys.stdin.readline


def pal(word):  # 팰린드롬 판정
    length = len(word) // 2
    for i in range(length):
        if word[i] != word[-i - 1]:  # 어떤 수 != 그 수의 숫자 순서를 뒤집은 수
            return False
    return True


def prime(number):  # 소수판정
    if number == 1:
        return False
    for i in range(2, int(math.sqrt(number)) + 1):  # 2부터 number의 제곱근까지의 모든 수를 확인하며
        if number % i == 0:  # number가 해당 수로 나눠떨어지면
            return False  # 소수가 아님
    return True


N = int(input())

while 1:
    if pal(str(N)) and prime(N):
        break
    N += 1
print(N)
