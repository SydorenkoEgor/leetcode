class Solution:
    def runningSum(self,nums:[])->[]:
        result:[]=[]
        for n in nums:
            numb = 0
            if len(result) != 0:
                numb = result[len(result)-1]
            result.append(n + numb)
        return result


print(Solution().runningSum([1,2,3,4]))