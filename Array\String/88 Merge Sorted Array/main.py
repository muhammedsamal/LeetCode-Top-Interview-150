class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j, k = (m + n) - 1, m - 1, n - 1

        while i > -1 and j > -1 and k > -1:
            if nums1[j] > nums2[k]:
                nums1[i] = nums1[j]
                j -= 1
            else:
                nums1[i] = nums2[k]
                k -= 1
            i -= 1
        while k > -1:
            nums1[i] = nums2[k]
            k -= 1
            i -= 1
