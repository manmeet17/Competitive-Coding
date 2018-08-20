class Solution:
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=1
        s=len(nums)
        p=[]
        k=0
        for j in range(s):
            if nums[j]>0:
                k+=1
                p.append(nums[j])
        for j in range(k):
            if abs(p[j])-1<k and p[abs(p[j])-1]>0:
                p[abs(p[j])-1]=-p[abs(p[j])-1]
        for j in range(k):
            if p[j]>0:
                return j+1
        return k+1
