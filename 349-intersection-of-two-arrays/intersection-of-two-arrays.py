class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        my_map={}
        seen=set()
        for i in nums1:
            my_map[i]=my_map.get(i,0)+1
        for i in nums2:
            if i in my_map:
                seen.add(i)
            else:
                continue
        return list(seen)

        