"""
Input: nums = [1,2,3,1]
Output: true
"""


def ind(nums: list[int]):

    dic = {}
    for value in nums:
        if value in dic:
            return True
        dic[value] = True
    return False


l = [2, 7, 11, 7]
print(ind(l))