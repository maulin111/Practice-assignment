from typing import List
import pytest


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]


@pytest.mark.parametrize('nums, target, ans',
                         [
                             [[2,7,11,15], 9, [0,1]],
                             [[3,2,4], 6, [1,2]]
                         ])
def test_twosum(nums, target, ans):
    assert Solution().twoSum(nums, target) == ans
