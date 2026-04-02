"""
Input: s = "Hello World"
Output: 5
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.split()[-1])

inp = "Hello World"
print(Solution().lengthOfLastWord(inp))