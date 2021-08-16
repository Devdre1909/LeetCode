class Solution:
    def singleNumber(self, nums):
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] = counts[num] + 1
            else:
                counts[num] = 0

        for num in counts:
            if(counts[num] == 0):
                return num


x = Solution().singleNumber([2, 2, 1])
print(x)
