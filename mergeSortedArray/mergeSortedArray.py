#Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
#Note:
#The number of elements initialized in nums1 and nums2 are m and n respectively.
#You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

     # First get rid of zeros
        while len(nums1) != m and nums1[-1]==0: nums1.pop()
        for i in range(len(nums2)):
            nums1.append(nums2[i])
            nums1.sort()

#l1=[-1,0,0,3,3,3,0,0,0]
#l2=[1,2,2]

#l1 = [1,2,3,0,0,0]
#l2 = [2,5,6]

#l1=[0]
#l2=[1]

l1=[-1,-1,0,0,0,0]
l2=[-1,0]

mergeLists = Solution()
mergeLists.merge(l1,4,l2,2)
print(l1)
