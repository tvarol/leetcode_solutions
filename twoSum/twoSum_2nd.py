class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dictList = {}
        for idx,value in enumerate(nums):
            complement = target - value
            if complement in dictList:
                return list((dictList[complement], idx))
                break
            dictList[value] = idx

        
myList = [9,5,6,4]
findSum = Solution()
findSum.twoSum(myList,13)
