class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l = len(nums)
        products = [1] * l

        for i in range(1, l):
            products[i] = products[i-1] * nums[i-1]
        right = nums[-1]
        for i in range(l-2, -1, -1):
            products[i] *= right
            right *= nums[i]
        return products