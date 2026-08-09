import heapq

class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        heap = []

        # Start with nums2[0] paired with first k elements of nums1
        for i in range(min(k, len(nums1))):
            heapq.heappush(heap, (nums1[i] + nums2[0], i, 0))

        ans = []

        while heap and len(ans) < k:
            total, i, j = heapq.heappop(heap)

            ans.append([nums1[i], nums2[j]])

            # Move to next element in nums2
            if j + 1 < len(nums2):
                heapq.heappush(
                    heap,
                    (nums1[i] + nums2[j + 1], i, j + 1)
                )

        return ans