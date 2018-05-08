#Given a string, find the length of the longest substring without repeating characters.
#Examples:
#Given "abcabcbb", the answer is "abc", which the length is 3.
#Given "bbbbb", the answer is "b", with the length of 1.
#Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
# Beats 35% of submissions, 130 ms. This is a sliding window question

class Solution:
    def lengthOfLongestSubstring(self,s):
        begin, end, length = 0, 0, 0
        phrase=""
        while begin < end+1 and end < len(s):
            if s[end] in phrase:
                begin += 1
                phrase = s[begin:end]
            else:
                end += 1
                phrase = s[begin:end]
                length = max(length,len(phrase))
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
