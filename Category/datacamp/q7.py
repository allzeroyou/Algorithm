# 7
score = int(input("점수를 입력하세요: "))


def getGrade(score):
    if score >= 90:
        grade = "A"
    elif 90 > score >= 80:
        grade = "B"
    elif 80 > score >= 70:
        grade = "C"
    elif 70 > score >= 60:
        grade = "D"
    else:
        grade = "F"

    print("성적은 " + grade + " 입니다.")


getGrade(score)
