class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        my_map={}
        for num in nums:
            my_map[num]=my_map.get(num,0) +1
        for count in my_map.values():
            if count>1:
                return True
        return False
        

        # if len(nums)<=0:
        #     return False
        # nums.sort()
        # for i in range(len(nums) - 1):
        #     if nums[i] == nums[i + 1]:
        #         return True
        # return False   
            
        # my_set=set(nums)
        # if len(my_set) == len(nums):
        #     return False
        # else:
        #     return True
        