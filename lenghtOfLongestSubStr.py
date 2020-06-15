class Solution:
    def lenghtOfLongestSubStr(self,s):
        characterByIndex = dict()
        maxLength = 0
        tempLength = 0
        index = 0
        while index < len(s):
            if s[index] in characterByIndex:
                item = characterByIndex.pop(s[index])
                index = item + 1

                if maxLength < tempLength:
                    maxLength = tempLength
                tempLength = 0
            else:
                characterByIndex[s[index]] = index
                tempLength += 1
            index+=1
        return maxLength;