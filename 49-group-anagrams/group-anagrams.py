class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        my_map={}
        for s in strs:
            sorted_str=''.join(sorted(s))

            if sorted_str not in my_map:
                my_map[sorted_str]=[]
        
            my_map[sorted_str].append(s)
        return list(my_map.values())
        # my_map={}
        # for i in strs:
        #     key = ''.join(sorted(i)) #sort the inside element i.e each string
        #     my_map.setdefault(key, []).append(i) #default key value pair & append values in map 
        # return list(my_map.values())
        

        