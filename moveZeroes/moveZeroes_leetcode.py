import time
start = time.time()

class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        count = nums.count(0)
        for i in range(count):
            nums.remove(0)
            nums.append(0)

nums = [0, 1, 0, 3, 12, 5, 0, 8]
mySolution = Solution()
mySolution.moveZeroes(nums)
print(nums)

end = time.time()
print(end-start)
