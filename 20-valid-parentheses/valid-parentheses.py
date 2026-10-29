class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        my_map={")":"(", "}":"{", "]":"["}

        for c in s:
            if c not in my_map:
                stack.append(c)
            else:
                if not stack:
                    return False
                else:
                    popped=stack.pop()
                    if popped!=my_map[c]:
                        return False
        return not stack


        