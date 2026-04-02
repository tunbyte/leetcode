"""
Input: a = "11", b = "1"
Output: "100"

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = []

        iA, iB = len(a) - 1, len(b) - 1

        while iA >= 0 or iB >= 0 or carry == 1:
            if iA >= 0:
                carry += int(a[iA])
                iA -= 1
            if iB >= 0:
                carry += int(b[iB])
                iB -= 1

            res.append(str(carry % 2))
            carry = carry // 2

        return "".join(res[::-1])

a = "11"
b = "1"

print(Solution().addBinary(a, b))