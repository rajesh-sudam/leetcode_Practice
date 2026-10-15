class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        my_map={}
        freq = []
        for i in range(len(nums)+1):
            freq.append([])
        for num in nums:
            my_map[num] = my_map.get(num, 0) + 1
        for n,c in my_map.items():
            freq[c].append(n)
        
        res=[]
        for bucket in reversed(freq):
            for n in bucket:
                res.append(n)
                if len(res)==k:
                    return res       

