class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, total = 0, 0
        res = float('inf')
        for i in range(len(nums)):
            total += nums[i] # add curr to total until total >= target
            while total >= target:
                total -= nums[l] #remove the first element of window
                res = min(res, i-l+1) # set the size of window
                l += 1 #change the starting position of the window since we removed the first element
        return 0 if res == float('inf') else res
        