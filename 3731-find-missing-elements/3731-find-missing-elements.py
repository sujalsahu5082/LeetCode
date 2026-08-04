from typing import List

class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        seen = set(nums)
        lo, hi = min(nums), max(nums)

        ans = []
        for x in range(lo, hi + 1):
            if x not in seen:
                ans.append(x)

        return ans