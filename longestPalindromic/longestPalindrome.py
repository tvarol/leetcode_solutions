class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        max_possible = len(s)
        
        for i in range(max_possible,0,-1):
            for j in range(0,max_possible-i+1):
                subs = s[j:j+i]
                print(s[j:j+i], j, j+i)
                if subs == subs[::-1]:
                    return subs
"""
    def longestPalindrome(self,strs):
        if len(strs) == 0: return ""
        elif len(strs)==1: return strs[0]

        begin, end = 0, len(strs)-1
        phrase = strs[begin:end+1]
        ans = ""       

        while begin<end and end<len(strs):
            phrase = strs[begin:end+1]
            if end==begin+1:
                begin += 1
                end = len(strs)
            print(phrase,begin,end)
            if phrase == phrase[::-1]:
                if len(phrase) > len(ans):
                    ans = phrase
            end -= 1
        if ans == "": return strs[len(strs)-1]
        return ans
"""
#strs = 'cbbd'
strs = 'babad'
#strs = ""
#strs = 'abb' 
#strs = 'bb'
#strs = 'abcda'
mySol = Solution()
print(mySol.longestPalindrome(strs))

                
