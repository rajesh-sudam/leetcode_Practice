class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        my_map={}
        for i in range(len(nums)):
            if nums[i] not in my_map:
                my_map[nums[i]]=[]

            my_map[nums[i]].append(i)
            arr=my_map[nums[i]]

            if len(arr)>=2:
                if abs(arr[-1]-arr[-2])<=k:
                    return True
        return False
        