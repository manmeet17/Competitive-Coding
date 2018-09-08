# Definition for an interval.
# class Interval(object):
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        l=[]
        if(len(intervals)==0 or len(intervals)==1):
            return intervals
        k=0
        for i in intervals:
            l.append((i.start,i.end))
            k+=1
        l=sorted(l)
        ans=[]
        curmax=l[0][1]
        curmin=l[0][0]
        for i in range(1,k):            
            if(l[i][0]<=curmax):
                curmax=max(curmax,l[i][1])
            elif l[i][0]>curmax:
                ans.append(Interval(curmin,curmax))
                curmin,curmax=l[i]
            if(i==k-1):
                ans.append(Interval(curmin,curmax))
            
        return (ans)
