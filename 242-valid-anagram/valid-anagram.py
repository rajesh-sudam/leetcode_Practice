class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map={}
        my_map1={}
        for char in s:
            my_map[char] =my_map.get(char, 0) + 1
        for char in t:
            my_map1[char]=my_map1.get(char, 0) + 1
        if my_map == my_map1:
            return True
        else:
            return False
        