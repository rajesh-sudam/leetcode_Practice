class Solution:
    def findMin(self, nums: list[int]) -> int:
        res= 5000
        for i in range(len(nums)):
            res=min(res,nums[i])
        return res
        