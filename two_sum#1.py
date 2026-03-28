"""

input: nums = [2, 7, 11, 15], target = 9
output: [0, 1]  ->  nums[0] + nums[1] = 9

"""


def solution(a: list[int], target: int):
    dic = {}

    for i, value in enumerate(a):
        remain = target - a[i]
        if remain in dic:
            return [i, dic[remain]]
        dic[value] = i



l = [2, 7, 11, 15]
print(solution(l, 9))
