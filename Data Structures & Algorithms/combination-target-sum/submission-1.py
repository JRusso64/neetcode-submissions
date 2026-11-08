class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def dfs(i, curr, currSum):
            if i >= len(nums) or currSum > target:
                return
            if currSum == target:
                res.append(curr.copy())
                return
            curr.append(nums[i])
            dfs(i, curr, currSum + nums[i])
            curr.pop()
            dfs(i+1, curr, currSum)
        dfs(0, [], 0)
        return res