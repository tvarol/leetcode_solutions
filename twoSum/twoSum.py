class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        from itertools import combinations
        for ((i,v1),(j,v2)) in combinations(enumerate(nums),2):
            if (v1+v2)==target:
                return list((i,j))
                break

myList = [5,6,7,8]
findSum = Solution()
findSum.twoSum(myList,13)
