class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # for i in range(len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if nums[i]+nums[j]==target:
        #             return [i,j]
        my_map={}
        for i in range(len(nums)): 
            diff = target - nums[i] # check if difference is present in hashmap
            if diff in my_map: 
                return i, my_map[diff] #if difference is found return indexes
                # break
            my_map[nums[i]] = i #if not set key and value in hashmap