class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1] * len(nums)
        postfix = [1] * len(nums)
        ans = []

        for i in range(len(nums)):
            if i==0:
                prefix[i]=nums[i]
            else:
                prefix[i]=prefix[i-1]*nums[i]
        for i in range(len(nums)-1,-1,-1):
            if i==len(nums)-1:
                postfix[i]=nums[i]
            else:
                postfix[i]=postfix[i+1]*nums[i]
        for i in range(len(nums)):
            if i==0:
                ans.append(postfix[i+1])
            elif i==len(nums)-1:
                ans.append(prefix[i-1])
            else:
                ans.append(prefix[i-1]*postfix[i+1])
        return ans

        