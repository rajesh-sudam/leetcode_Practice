class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        count=1
        longest=1
        if len(nums)==0:
            return 0
        for i in range(len(nums)):
            if i ==0:
                continue
            if nums[i] == nums[i-1]:
                continue
            
            if nums[i]==nums[i-1]+1:
                count+=1
            else:
                longest=max(count,longest)
                count=1
        return max(longest,count)