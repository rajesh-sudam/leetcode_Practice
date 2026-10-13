class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:

        if len(nums)<=0:
            return False
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False   
            
        # my_set=set(nums)
        # if len(my_set) == len(nums):
        #     return False
        # else:
        #     return True
        