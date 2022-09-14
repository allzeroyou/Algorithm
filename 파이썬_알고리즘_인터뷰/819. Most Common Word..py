import collections
from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        paragraph=re.sub('[^\w]',' ',paragraph) # ^는 반대 의미. 단어가 아닌 것을 공백처리
        words = paragraph.split()

        voca = collections.defaultdict(int) # 단어 세기

        for word in words:
            if word not in banned:
                voca[word]+=1

        return max(voca, key=voca.get) # .get -> value 최댓값을 기준으로 key 출력



s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
