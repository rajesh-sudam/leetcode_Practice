from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1

        count = 1
        count1 = 1

        max_count = 1
        max_count1 = 1

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                count += 1
                count1 = 1

            elif nums[i] > nums[i + 1]:
                count1 += 1
                count = 1

            else:
                count = 1
                count1 = 1

            max_count = max(max_count, count)
            max_count1 = max(max_count1, count1)

        return max(max_count, max_count1)
