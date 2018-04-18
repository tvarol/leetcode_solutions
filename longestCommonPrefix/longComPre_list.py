class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs)==0:
            return ""
        elif len(strs)==1:
            return strs[0]

        strs.sort(key = len, reverse=True)
        print(strs)

        if len(strs)==0:
                return ""
        elif len(strs)==1:
            phrase = strs[0]

        phrase = ""
        check_phrase = strs[0]
        for j in range(1, len(strs)):
            for i in range(len(check_phrase),0,-1):
                count = 0
                if strs[j].startswith(check_phrase[0:i]):
                    check_phrase = check_phrase[0:i]
                    phrase = check_phrase
                    count += 1
                    break
                if i==1 and count==0:
                    return ""
                    
        return phrase
                
myList= ["",""]

findLongPre = Solution()
print(findLongPre.longestCommonPrefix(myList))
