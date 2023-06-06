# 학생 n명의 이름과 국,영,수 점수
# 다음 조건으로 학생 성적 정렬
# 1. 국어점수가 감소하는 순서로
# 2. 국어점수가 같으면 영어 점수가 증가하는 순서로
# 3. 국어점수와 영어 점수가 같으면 수학 점수가 감소하는 순서로
# 4. 모든 점수가 같으면 이름이 사전순으로 증가하는 순서로(대문자<소문자)

n = int(input())

student = []

for i in range(n):
    input_data = input().split()
    student.append((input_data[0], int(input_data[1]), int(input_data[2]), int(input_data[3])))  # 튜플로 저장

# 튜플은 원소의 순서에 맞게 정렬되는 특징이 있음!
student = sorted(student, key=lambda s: (-s[1], s[2], -s[3], s[0]))

for s in student:
    print(s[0])
