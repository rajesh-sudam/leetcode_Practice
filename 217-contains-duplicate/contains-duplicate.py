class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        my_set=set(nums)
        if len(my_set) == len(nums):
            return False
        else:
            return True
        