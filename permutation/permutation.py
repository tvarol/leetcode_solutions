class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        from itertools import permutations
        return list(permutations(nums, len(nums)))

myList = [1,2,3]
findPerm = Solution()
findPerm.permute(myList)
