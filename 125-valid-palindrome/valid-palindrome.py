class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        cleaned=""
        for char in s:
            if char.isalnum():
                cleaned+=char
        reverse=''.join(reversed(cleaned))
        return reverse == cleaned
        