class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        for i, a in enumerate(nums):
            if i > 0 and nums[i-1] == a: # skip same elems
                continue
            
            l, r = i, len(nums) - 1

            while l < r:
                # calc 3sum
                threeSum = a + nums[l] + nums[r]

                if threeSum < 0:
                    l += 1
                elif threesum > 0:
                    r -= 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l < r: # avoid dups
                        l += 1
            return res
        