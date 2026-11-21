class Solution:
    def sortedSquares(self, nums: list[int]) -> list[int]:
        for i in range(len(nums)):
            nums[i]=nums[i]*nums[i]
        nums.sort()
        return nums
        # arr=[]
        # for i in range(len(nums)):
        #     arr.append(nums[i]*nums[i])
        # arr.sort()
        # return arr
        