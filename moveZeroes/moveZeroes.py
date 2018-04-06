import time
start = time.time()

class Solution:
    def moveZeroes(self, nums):
        index_list_zero = [i for i, j in enumerate(nums) if j == 0]
        count_zero = 0
        for idx in index_list_zero:
            if idx==0:
                 nums[:] = nums[1:] + nums[:1]
            else:
                n = idx-count_zero
                nums[:] = nums[:n] + nums[n+1:] + nums[n:n+1]
            count_zero += 1
        print(nums)    

nums = [0, 1, 0, 3, 12, 5, 0, 8]

mySolution = Solution()
mySolution.moveZeroes(nums)
print(nums)

end = time.time()
print(end-start)
