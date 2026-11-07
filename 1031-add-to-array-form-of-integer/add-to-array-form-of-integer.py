class Solution:
    def addToArrayForm(self, num: list[int], k: int) -> list[int]: 
        sum=0
        res=[]
        for n in num:
            sum=sum*10+n
        sum+=k
        while sum>0:
            res.append(sum%10)
            sum//=10
        res.reverse()
        return res