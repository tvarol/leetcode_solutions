import random
class Solution:
    def pickIndex(self,nums):
        total = sum(nums)
        rndm = random.uniform(0,1)

        for i,val in enumerate(nums):
            nums[i] = val/total
            if rndm < sum(nums[:i+1]):
                return i
            
        #rnd = random.uniform(0,1)
        #for i in range(len(nums)):
         #   if rnd < sum(nums[:i+1]):
          #      return i


nums = [1,2,3]
mySol = Solution()
print(mySol.pickIndex(nums))
