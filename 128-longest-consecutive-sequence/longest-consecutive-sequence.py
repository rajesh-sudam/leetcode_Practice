class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        current=1
        longest=1

        if len(nums)==0:
            return 0
        
        for i in range(len(nums)):
            if i==0:
                continue
            if nums[i]==nums[i-1]:
                continue
            elif (nums[i]==nums[i-1]+1):
                current+=1
                longest=max(current,longest)
            else:
                current=1
        return max(current,longest)
            

            