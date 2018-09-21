from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        d=defaultdict(list)
        for i in range(len(strs)):
            s=''.join(sorted(strs[i]))
            if s in d:
                d[s].append(i)
            else:
                d[s]=[i]
        ans=[]
        for i,j in d.items():
            ans.append([strs[x] for x in j])
        return ans
