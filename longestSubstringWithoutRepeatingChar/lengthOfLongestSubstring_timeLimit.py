class Solution:
    def lengthOfLongestSubstring(self,s):
        if len(s)==0: return 0
        elif len(s)==1: return 1
        elif len(s)==2 and s[0]!=s[1]: return 2
        
        phrase = s[0]
        length = 0

        i = 1
        while i < len(s):
            if s[i] in phrase: 
                if len(phrase) > length:
                    length = len(phrase)
                phrase = s[i-1]
            else:
                phrase += s[i]
                if i==len(s)-1 and len(phrase) > length:
                    length = len(phrase)
                i += 1
        return length

strng ="dvdf"
#strng = "aab"
#strng = "au"
#strng = "bbbbb"
#strng = "pwwkew"
#strng = "abcabcbb"
mySol = Solution()
mySol.lengthOfLongestSubstring(strng)
print(mySol.lengthOfLongestSubstring(strng))
