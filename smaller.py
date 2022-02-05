class Solution:
    def smallerNumbersThanCurrent(self, nums: list[int]) -> list[int]:
        rl=[0]*len(nums)
        x=0
        for i in nums:
            for j in nums:
                if(j < i):
                    rl[x]+=1
            x+=1
        return rl

s = Solution()
a = s.smallerNumbersThanCurrent([6,6,6,6])
print(a)
