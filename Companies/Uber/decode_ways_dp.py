class Solution:
    def valid(self,_s):
        if int(_s) <= 26:
            return 1
        return 0

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        if(n==0):
            return 0

        if s.startswith('0') or s.find('00') != -1:
            return 0

        dp = [0 for i in range(n+1)]
        dp[0],dp[1] = 1,1

        for i in range(2,n+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if s[i-2] == '1' or (s[i-2] == '2' and s[i-1] < '7'):
                dp[i] += dp[i-2]

        return(dp[n])

