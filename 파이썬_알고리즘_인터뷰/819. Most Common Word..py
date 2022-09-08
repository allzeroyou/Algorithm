from typing import List
import re

class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph=paragraph.lower()
        paragraph=re.sub('[^a-z0-9]','',paragraph)
        print(paragraph)


s = Solution()
print(s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", banned = ["hit"]))
