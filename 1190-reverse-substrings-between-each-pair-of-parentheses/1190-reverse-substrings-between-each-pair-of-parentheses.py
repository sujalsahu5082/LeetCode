class Solution:
    def reverseParentheses(self, s):
        stack = [[]]

        for ch in s:
            if ch == '(':
                stack.append([])

            elif ch == ')':
                current = stack.pop()
                current.reverse()
                stack[-1].extend(current)

            else:
                stack[-1].append(ch)

        return ''.join(stack[0])