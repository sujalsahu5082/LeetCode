class Solution:
    def summaryRanges(self, nums):
        ans = []
        i = 0

        while i < len(nums):
            start = nums[i]

            while i + 1 < len(nums) and nums[i + 1] == nums[i] + 1:
                i += 1

            if start == nums[i]:
                ans.append(str(start))
            else:
                ans.append(str(start) + "->" + str(nums[i]))

            i += 1

        return ans