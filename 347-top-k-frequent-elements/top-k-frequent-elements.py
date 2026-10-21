class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        my_map = {}

        for n in nums:
            my_map[n] = my_map.get(n, 0) + 1

        freq = [[] for _ in range(len(nums) + 1)]

        for n, count in my_map.items():
            freq[count].append(n)

        res = []

        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res