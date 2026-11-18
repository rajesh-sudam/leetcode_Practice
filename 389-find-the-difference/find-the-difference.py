class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        stack=list(s)

        for ch in t:
            if ch in stack:
                stack.remove(ch)
            else:
                return ch
        