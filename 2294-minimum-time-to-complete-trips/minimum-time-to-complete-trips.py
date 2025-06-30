class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        def possible(time,giventime,totalTrips):
            actualtime=0
            for t in time:
                actualtime+=giventime//t
            return (actualtime>=totalTrips)





        l=1
        r=totalTrips*min(time)

        while l<r:
            midTime=(r+l)//2

            if possible(time,midTime,totalTrips):
                r=midTime
            else:
                l=midTime+1
        return l