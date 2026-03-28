"""
Input: strs = ["flower","flow","flight"]
Output: "fl"

Input: strs = ["dog","racecar","car"]
Output: ""

"""


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for word in strs:
                if i >= len(word) or word[i] != char:
                    return res
            res += char
        return res





inp = ["flower","flow","flight"]

sol = Solution().longestCommonPrefix(inp)
print(sol)