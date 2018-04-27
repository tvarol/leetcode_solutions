# Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.
# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Accepted but takes 1800 ms, so long
        if(len(nums)) == 0: return
        if(len(nums)) == 1: return(len(nums))
        for i in reversed(range(len(nums))):
            if(nums[i] == nums[i-1] and len(nums)!=1):
                nums.remove(nums[i])
        return(len(nums))

        # BELOW ARE THE OTHER WAYS OF SOLVING THIS PROBLEM
        # This works and beats 88.1% python submissions. But list(set()) creates a copy allocating O(n)
        """
        nums[:] = sorted(list(set(nums)))
        return(nums)
        """

        # This works but leetcode doesn't accept numpy
        """
        import numpy as np
        nums[:] = np.unique(nums)
        return(len(nums))
        """

        # Time Limit Exceeded in the Example Below
        """
        for i in nums:
            if nums.count(i) == 1: continue
            while(nums.count(i) > 1 ):
                nums.remove(i)
        return(len(nums))
        """

        # Serhan's Solution
        """
        for idx,number in enumerate(nums):
            while idx+1 < len(nums) and number == nums[idx+1]:
                del nums[idx]
        return(len(nums))
        """
            
#myList = [-1,0,0,0,0,3,3]
myList = [1,1]

remDup = Solution()
print(remDup.removeDuplicates(myList))
