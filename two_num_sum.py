from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(0, len(nums)):
            current = nums[i]
            for j in range(i + 1, len(nums)):
                if current + nums[j] == target:
                    return [i, j]


nums = [2, 7, 11, 15]
target = 9
Solution().twoSum(nums, target)
