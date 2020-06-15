class Solution:
    def findPoisonedDuration(self, timeSeries:[int], duration: int) -> int:
        pDuration = 0
        starttime = 0
        endtime = 0
        for i in timeSeries:
            stime = i
            etime = stime + duration
            if stime >= endtime:
                pDuration += etime - stime
            else :
                pDuration += etime - endtime

            starttime = stime
            endtime = etime
        return pDuration

