#Given a 32-bit signed integer, reverse digits of an integer.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
# Beats 54% of submissions, 59 ms

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        
        if x > 0:
            x = int(str(x)[::-1])
        else:
            x = -int(str(abs(x))[::-1])
        
        if x >= 2**31 - 1 or x <= -2**31:
            return 0
        else:
            return x

"""
ALTERNATIVE SOLUTION, BEATS 80% OF SUBMISSIONS, 55 MS
class Solution(object):
    def reverse(self, x):
        n = abs(x)
        res = 0
        while n!=0:
            a = n%10
            n = n//10
            res = res*10+a
        
        if res >= 2**31 - 1 or res <= -2**31:
            return 0
        elif x > 0:
            return res
        else:
            return -res        
"""
