class Solution:
    def checkString(self, s: str) -> bool:
        for ch in range(len(s)-1):
            if s[ch]=='b' and s[ch+1]=='a':
                return False
            else:
                continue
        return True
        