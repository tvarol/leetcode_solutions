#There are two sorted arrays nums1 and nums2 of size m and n respectively.
#Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
# Beats 99.47% of submissions
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums1.extend(nums2)
        nums1.sort()
        if len(nums1)%2==0:
            el1 = int(len(nums1)/2)
            return float(nums1[el1]+nums1[el1-1])/2
        else:
            return nums1[len(nums1)//2]



nums1 = [1,2]
nums2 = [3,4]
mySol = Solution()
print(mySol.findMedianSortedArrays(nums1,nums2))
