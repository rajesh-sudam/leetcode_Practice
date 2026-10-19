class Solution:
    def isPalindrome(self, s: str) -> bool:
        # s=''.join(ch.lower() for ch in s  if ch.isalnum())
        # str=""
        # for ch in s:
        #     if ch.isalnum():
        #         str+=ch
        # s=s.lower()
        # cleaned=""
        # for char in s:
        #     if char.isalnum():
        #         cleaned+=char
        # reverse=''.join(reversed(cleaned))
        # return reverse == cleaned

        s=''.join(ch.lower() for ch in s if ch.isalnum())
        l=0
        r=len(s)-1

        while l<r:
            if s[l]!=s[r]:
                return False
            l+=1
            r-=1
        return True
        