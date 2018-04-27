#Given an array, rotate the array to the right by k steps, where k is non-negative.
#Beats 82% of submissions, 70 ms 

class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        a = len(nums)
        nums.extend(nums[:a-k%a])
        del nums[:a-k%a]
        
myList=[1,2,3,4,5,6,7]
rot = Solution()
rot.rotate(myList,10)
print(myList)

# ALTERNATIVE SOLUTIONS

# Beats 1% of solutions, 319 ms
"""
if len(nums) == 0: return
for i in xrange(k):
    nums.insert(0,nums[-1])
    del nums[-1]
"""

# Beats 82% of submissions, 70 ms
"""
nums[:] = nums[len(nums)-k:] + nums[:len(nums)-k]
"""
