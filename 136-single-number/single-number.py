class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        my_map={}
        for i in range(len(nums)):
            my_map[nums[i]]=my_map.get(nums[i],0)+1
        for keys,values in my_map.items():
            if values==1:
                return keys
        return 0