n = int(input())

student = []


for i in range(n):
    input_data = input().split()
    student.append((input_data[0],int(input_data[1]), int(input_data[2]), int(input_data[3]))) # 튜플로 저장

# 튜플은 원소의 순서에 맞게 정렬되는 특징이 있음!
student = sorted(student, key=lambda s: (-s[1], s[2], -s[3], s[0])) 


for s in student:
    print(s[0])