class Solution:
    def lengthLongestPath(self, input: str) -> int:
        stack = [0]  # stack[level] = total length up to that level
        ans = 0

        for line in input.split("\n"):
            level = line.count("\t")
            name = line.lstrip("\t")

            while len(stack) > level + 1:
                stack.pop()

            curr_len = stack[-1] + len(name)

            if "." in name:
                ans = max(ans, curr_len)
            else:
                stack.append(curr_len + 1)  # +1 for '/'

        return ans