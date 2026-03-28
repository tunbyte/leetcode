"""
Input: s = "()[]{}"
Output: true
"""


class Solution:
    def isValid(self, x: str) -> bool:
        stack = []
        pars = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for char in x:
            if char in "({[":
                stack.append(char)
            else:
                if stack and stack[-1] == pars[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0

inp = ""

sol = Solution().isValid(inp)
print(sol)