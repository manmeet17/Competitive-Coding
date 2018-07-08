class Solution:
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        m=[1]*n
        for i in range(1,n):
            for j in range(0,i):
                if nums[j]<nums[i]:
                    m[i]=max(m[i],1+m[j])
                    
        return max(m)

def stringToIntegerList(input):
    return json.loads(input)

def main():
    import sys
    def readlines():
        for line in sys.stdin:
            yield line.strip('\n')

    lines = readlines()
    while True:
        try:
            line = next(lines)
            nums = stringToIntegerList(line);
            
            ret = Solution().lengthOfLIS(nums)

            out = str(ret);
            print(out)
        except StopIteration:
            break

if __name__ == '__main__':
    main()