class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        my_map={}
        for ch in s:
            my_map[ch]=my_map.get(ch,0)+1
        for ch in t:
            if ch not in my_map:
                return False
            my_map[ch]-=1
        
        for count in my_map.values():
            if count!=0:
                return False
        return True


        # return ''.join(sorted(s)) == ''.join(sorted(t))
        # my_map={}
        # my_map1={}
        # for char in s:
        #     my_map[char] =my_map.get(char, 0) + 1
        # for char in t:
        #     my_map1[char]=my_map1.get(char, 0) + 1
        # if my_map == my_map1:
        #     return True
        # else:
        #     return False
        