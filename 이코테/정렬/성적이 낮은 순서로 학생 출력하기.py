# n명의 학생 수
# 학생의 이름과, 학생의 성적
# 성적인 낮은 순으로 학생의 이름을 출력하는 프로그램

n = int(input())
score= []
for i in range(n):
    name_score = input().split() # 띄어쓰기를 기준으로 잘라서 배열로 만듬.
    score.append(name_score[1])

score = sorted(score)


'''
2
홍길동 95
이순신 77
'''
