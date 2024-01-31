import collections
from typing import List
import re


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i, n in enumerate(nums):
            ans = target - n # 두수의 합이니까!
            #print(f'i: {i}, n: {n}, ans:{ans}')
            if ans in nums[i + 1:]:

                return [nums.index(n), nums[i+1:].index(ans)+(i+1)] # 3,3 같은 배열을 고려해야


s = Solution()
print(s.twoSum([3,3], 6))
