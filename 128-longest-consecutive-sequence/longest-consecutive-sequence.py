class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums.sort()
        longest=1
        current=1

        if len(nums)==0:
            return 0

        for i in range(len(nums)):
            if i==0:
                continue
            if nums[i]==nums[i-1]:
                continue
            if nums[i]==nums[i-1]+1:
                current+=1
            else:
                longest=max(current,longest)
                current=1
        return max(longest,current)
            

            