"""
Input: s = "LVIII"
Output: 58

Input: s = "III"
Output: 3

"""


class Solution:
    def romanToTnt(self, s: str) -> int:
        roman_nums = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        v = 0
        for i in range(len(s)):
            if i+1 < len(s) and roman_nums[s[i]] < roman_nums[s[i+1]]:
                v -= roman_nums[s[i]]
            else:
                v += roman_nums[s[i]]

        return v


inp = "LVIII"

sol = Solution().romanToTnt(inp)
print(sol)