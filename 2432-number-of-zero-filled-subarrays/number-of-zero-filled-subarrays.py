class Solution:
    def zeroFilledSubarray(self, nums: list[int]) -> int:
        l=0
        res=0
        for r in range(len(nums)):
            if nums[r]!=0:
                l=r+1
            res+=r-l+1
        return res