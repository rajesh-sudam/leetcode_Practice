class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        l=0
        maxcount=0
        maxlength=0

        for r in range(len(s)):
            count[s[r]]=count.get(s[r],0)+1
            maxcount=max(maxcount,count[s[r]])

            windowlen=r-l+1
            if windowlen - maxcount >k:
                count[s[l]]-=1
                l+=1
            
            maxlength=max(maxlength,r-l+1)
        return maxlength
