class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stack = []

        for i,c in enumerate(s):
            if c == '(':
                stack.append(i)

            else:
                if len(stack) >= 1 and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)

        if len(stack) == 0:
            return(len(s))
        else:

            maxi = 0
            l = 0

            for i in stack:
                maxi = max(maxi, i - l)
                l = i + 1

            maxi = max(maxi, len(s) - l)
            return maxi
