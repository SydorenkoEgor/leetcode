class Solution:
    def findLeastNumOfUniqueInts(self, arr: [int], k: int) -> int:
        dc:dict = dict()

        for i in arr:
            dc[i] = 1 if i not in dc else dc[i] + 1

        sItems = sorted(dc.values())
        deletedCounter = 0
        for i in sItems:
            if k == 0:
                break

            if i > k:
                k=0
            else:
                k-=i
                deletedCounter+=1
        return len(sItems) - deletedCounter

print(Solution().findLeastNumOfUniqueInts([5,5,4],1))
#1,1,3,3,8]
#2,4,1,8,3,5,1,3]
