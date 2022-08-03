'''
두개의 배열 A,B은 N개의 원소로 구성됨
배열의 원소는 모두 자연수
최대 K번의 바꿔치기 연산 수행 가능
바꿔치기란 배열 A에 있는 원소 하나와 배열 B에 있는 원소 하나를 골라서 두 원소를 서로 바꾸는 것을 의미

최종목표: 배열 A의 모든 원소의 합이 최대가 되도록 함

N,K 그리고 배열 A,B의 정보 -> 최대 K번 바꿔치기 연산 수행 -> 만들 수 있는 배열 A의 모든 원소의 합의 최댓값 출력

ex. N=5, K=3이고 배열 A,B가 다음과 같음
A=[1,2,5,4,3]
B=[5,5,6,6,5]
다음과 같이 세번의 연산 수행 가능
연산1) 배열 A의 원소 '1'과 배열 B의 원소 '6' 바꾸기
연산2) 배열 A의 원소 '2'과 배열 B의 원소 '6' 바꾸기
연산3) 배열 A의 원소 '3'과 배열 B의 원소 '5' 바꾸기
세번 연산 후
A=[6,6,5,4,5]
B=[3,5,1,2,5]
이때 배열 A의 모든원소 합은 26, 더 크게 합을 만들 수는 없음
'''
import sys

N, K= map(int, input().split())
A=[]
B=[]
a_data = sys.stdin.readline().rstrip()
a_data = a_data.split()
for i in a_data:
    A.append(int(i))

b_data = sys.stdin.readline().rstrip()
b_data = b_data.split()
for i in b_data:
    B.append(int(i))

A.sort()
B.sort(reverse=True)

for i in range(K):
    A[i]=B[i]

print(sum(A))