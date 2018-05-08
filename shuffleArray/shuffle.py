# Shuffle a set of numbers without duplicates.
# 95% beats submission
# Kopyalamak icin import copy deyip sonra copy.copy(nums) yapabilirsin. Ya da direkt list()'te kopyasini veriyor ama [:] daha hizli.


import random
class Solution:
    def __init__(self, nums):
        self.array = nums
        self.original = nums[:]

    def reset(self):
        self.array = self.original[:]
        return self.array

    def shuffle(self):
        random.shuffle(self.array)
        return self.array

nums = [1,2,3]
mySol = Solution(nums)
print(mySol.shuffle())
print(mySol.reset())

"""
Serhan's random shuffle definition
def shuffle(nums):
    for idx in xrange(len(nums)-1,1,-1):
        jdx  = random.randint(0,idx) 
        temp = nums[idx]
        nums[idx] = nums[jdx]
        nums[jdx] = temp

Another solution from leetcode:
def shuffle(self):
    for i in range(len(self.array)):
        swap_idx = random.randrange(i, len(self.array))
        self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array


"""
