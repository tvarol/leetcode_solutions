import time
start = time.time()

class Solution(object):
    def moveZeroes(self,nums):
        internal = [x for x in nums if x!=0]
        internal.extend([0]*(len(nums)-len(internal)))
        nums[:] = internal


nums = [0, 1, 0, 3, 12, 5, 0, 8]

mySolution = Solution()
mySolution.moveZeroes(nums)
print(nums)

end = time.time()
print(end-start)
