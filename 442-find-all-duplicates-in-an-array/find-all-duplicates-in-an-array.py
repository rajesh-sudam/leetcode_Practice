class Solution:
    def findDuplicates(self, nums: list[int]) -> list[int]:
        my_map={}
        arr=[]
        for i in range(len(nums)):
            my_map[nums[i]]=my_map.get(nums[i],0)+1

        for keys, values in my_map.items():
            if values==2:
                arr.append(keys)

        return arr
        
        