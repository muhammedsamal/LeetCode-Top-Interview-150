class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        for i in range(len(nums)):
            if i < len(nums) - 2 and nums[i] == nums[i+2]:
                continue
            nums[k] = nums[i]
            k += 1
        return k    