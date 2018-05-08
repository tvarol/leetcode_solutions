"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.

Beats 37% of submissions, 194 ms
"""


class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        roman = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        
        if len(s)==1: return roman[s[0]]
        
        tot = 0
        for i in range(1,len(s)):
            if roman[s[i]] > roman[s[i-1]]:
                if s[i-1]=="I":
                    tot -= 1
                elif s[i-1]=="X":
                    tot -= 10
                elif s[i-1]=="C":
                    tot -= 100
                
                if i == len(s)-1: tot += roman[s[i]]
            else:
                tot += roman[s[i-1]]
                if i == len(s)-1: tot += roman[s[i]]
                    
        return tot

"""
ALTERNATIVE SOLUTION, BEATS 74% SUBMISSIONS (MY SUBMISSION OF THIS CODE: BEATS 42% )
class Solution:
    def romanToInt(self, s):
        res=0
        dic = {'M':1000,'CM':900,'D':500,'CD':400,'C':100,'XC':90,'L':50,'XL':40,'X':10,'IX':9,'V':5,'IV':4,'I':1}
        while len(s)!=0:
            if s[:2] in dic:
                res += dic[s[:2]]
                s = s[2:]
            elif s[:1] in dic:
                res += dic[s[:1]]
                s = s[1:]
        return res
"""
