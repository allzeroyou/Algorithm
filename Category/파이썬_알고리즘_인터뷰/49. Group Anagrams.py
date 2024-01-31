import collections
from typing import List
import re


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # 존재하지 않는 키를 삽입하려 할 경우 KeyError 발생
        # -> 에러 발생하지 않도록 디폴트 생성해주는 defaultdict()로 선언
        anagrams = collections.defaultdict(list)
        for word in strs:
            # 에너그램 단어 판단: 정렬하면 서로 같은 값
            anagrams[''.join(sorted(word))].append(word)
        return list(anagrams.values())


s = Solution()
print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))
