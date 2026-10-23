class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        availableNums = set(nums)
        res = 0
        for n in nums:
            if n - 1 not in availableNums:
                currNum = n
                currLen = 1
                while currNum + 1 in availableNums:
                    currLen += 1
                    currNum += 1
                res = max(res, currLen)
        return res
                