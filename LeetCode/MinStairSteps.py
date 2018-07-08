class Solution:
    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        mcost=[cost[0],cost[1]]+[0]*(len(cost)-2)
        for i in range(2,len(cost)):
            mcost[i]=min(mcost[i-1]+cost[i],mcost[i-2]+cost[i])
        return min(mcost[-1],mcost[-2])