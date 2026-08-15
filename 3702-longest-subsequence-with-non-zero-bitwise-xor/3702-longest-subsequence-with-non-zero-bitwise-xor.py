class Solution:
    def longestSubsequence(self, nums):
        xor_all = 0
        has_non_zero = False

        for num in nums:
            xor_all ^= num
            if num != 0:
                has_non_zero = True

        if xor_all != 0:
            return len(nums)

        if has_non_zero:
            return len(nums) - 1

        return 0