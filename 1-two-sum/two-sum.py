class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        my_map = {}

        for i in range(len(nums)):
            difference = target - nums[i]

            if difference in my_map:
                return [my_map[difference], i]

            my_map[nums[i]] = i
                