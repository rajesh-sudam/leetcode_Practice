class Solution:
    def getNoZeroIntegers(self, n: int) -> list[int]:
        for i in range(1,n):
            a=i
            b=n-i

            if '0' not in str(a) and '0' not in str(n-i):
                return [a,b]
        return []




        