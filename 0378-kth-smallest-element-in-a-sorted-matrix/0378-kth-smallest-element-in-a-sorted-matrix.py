class Solution:
    def kthSmallest(self, matrix, k):
        n = len(matrix)

        low = matrix[0][0]
        high = matrix[n - 1][n - 1]

        while low < high:
            mid = (low + high) // 2

            count = self.countLessEqual(matrix, mid)

            if count < k:
                low = mid + 1
            else:
                high = mid

        return low

    def countLessEqual(self, matrix, target):
        n = len(matrix)

        row = n - 1
        col = 0
        count = 0

        while row >= 0 and col < n:
            if matrix[row][col] <= target:
                # Everything above this element is also <= target
                count += row + 1
                col += 1
            else:
                row -= 1

        return count