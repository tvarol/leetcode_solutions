#Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.
# Beats 70% of python submissions, 99 ms
# Beats 91% of python submissions when import is outside of the class and with list comprehension, 89 ms
import random
class Solution(object):

    def __init__(self, nums):
        """
        
        :type nums: List[int]
        :type numsSize: int
        """

        self.nums = nums        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        #index = []
        index = [idx for idx,value in enumerate(self.nums) if value==target]
        #for idx,value in enumerate(self.nums):
         #   if value==target:
          #      index.append(idx)
        return random.choice(index)


# Your Solution object will be instantiated and called as such:
nums = [1,2,3,3,3]
obj = Solution(nums)
param_1 = obj.pick(3)
print(param_1)
