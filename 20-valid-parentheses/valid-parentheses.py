class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        my_map={")":"(","}":"{","]":"["}

        for char in s:
            if char in my_map.values():
                stack.append(char)
            elif char in my_map.keys():
                if not stack or my_map[char]!=stack.pop():
                    return False
        return not stack

        