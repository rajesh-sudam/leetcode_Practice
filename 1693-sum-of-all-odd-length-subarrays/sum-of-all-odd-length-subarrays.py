class Solution:
    def sumOddLengthSubarrays(self, arr: list[int]) -> int:
        s=0
        for i in range(len(arr)):
            for j in range(i,len(arr)):
                if len(arr[i:j+1])%2==1:
                    s+=sum(arr[i:j+1])
        return s

                
        