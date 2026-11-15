class Solution:
    def kidsWithCandies(self, candies: list[int], extraCandies: int) -> list[bool]:
        res=[]
        n=max(candies)
        for i in candies:
            if i+extraCandies>=n:
                res.append(1==1)
            else:
                res.append(1!=1)
        return res