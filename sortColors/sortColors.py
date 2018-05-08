#Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.
#Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.
#Note: You are not suppose to use the library's sort function for this problem.

# https://leetcode.com/problems/sort-colors/discuss/26481/Python-O(n)-1-pass-in-place-solution-with-explanation
# Beats 78% of submissions, 37 ms
class Solution:
    def sortColors(self,nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        r = 0 #index of red
        w = 0 # index of white
        b = len(nums)-1 # index of blue

        while w <= b:
            if nums[w] == 0:
                nums[r], nums[w] = nums[w], nums[r]
                w += 1
                r += 1
            elif nums[w] == 1:
                w += 1
            else:
                nums[w], nums[b] = nums[b], nums[w]
                b -= 1

nums = [2,0,2,1,1,0]
mySol = Solution()
mySol.sortColors(nums)
print(nums)
"""
 # Beats 8%, 57 ms
for idx in range(1, len(nums)):
    while idx > 0 and nums[idx-1] > nums[idx]:
        nums[idx-1], nums[idx] = nums[idx], nums[idx-1]
        idx -= 1
"""
