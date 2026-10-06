class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        # nums1.extend(nums2)
        # while 0 in nums1:
        #     nums1.remove(0)

        # while nums1:
        #     if nums1[0] == 0:
        #         nums1.pop(0)
        #     elif nums1[-1] == 0:
        #         nums1.pop()
        #     else:
        #         break 
        nums1.sort()

                
        