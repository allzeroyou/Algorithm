from typing import List

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        word_lst = []
        digit_lst = []
        for i in logs:
            idf = i.split() # 띄어쓰기 분리
            if idf[1].isdigit(): # 숫자 로그 판별
                digit_lst.append(i)
            else:
                word_lst.append(i)
        word_lst.sort(key=lambda x:(x.split()[1:], x.split()[0])) # 문자가 동일한 경우 식별자 순으로
        # 람다는 sort()의 예와 같이 함수와 함께 사용하는 것이 일반적인 용도임
        return word_lst+digit_lst




s = Solution()
print(s.reorderLogFiles(["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]))
