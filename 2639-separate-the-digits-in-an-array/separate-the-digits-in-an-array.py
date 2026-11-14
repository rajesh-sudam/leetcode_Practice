class Solution:
    def separateDigits(self, nums: list[int]) -> list[int]:
        arr = []

        for i in nums:
            temp = []

            while i > 0:
                temp.append(i % 10)
                i //= 10

            arr.extend(temp[::-1])

        return arr