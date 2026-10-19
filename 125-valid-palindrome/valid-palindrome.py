class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        str=""
        for ch in s:
            if ch.isalnum():
                str+=ch

        l=0
        r=len(str)-1
        while l<r:
            if str[l]!=str[r]:
                return False
            l+=1
            r-=1

        return True
        # s=s.lower()
        # cleaned=""
        # for char in s:
        #     if char.isalnum():
        #         cleaned+=char
        # reverse=''.join(reversed(cleaned))
        # return reverse == cleaned
        