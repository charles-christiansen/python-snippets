## Find smaller numbers than the current number in a list
## LeetCode: https://leetcode.com/problems/how-many-numbers-are-smaller-than-the-current-number/
## Given a list of numbers, return a list containing the count
## of numbers in the list smaller than the number at each index
from typing import List
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        rl=[0]*len(nums)
        x=0
        for i in nums:
            for j in nums:
                if(j < i):
                    rl[x]+=1
            x+=1
        return rl

s = Solution()
# Returns [4,0,1,1,3]
print(s.smallerNumbersThanCurrent([8,1,2,2,3]))
# Returns [2,1,0,3]
print(s.smallerNumbersThanCurrent([6,5,4,8]))
# Returns [0,0,0,0]
print(s.smallerNumbersThanCurrent([6,6,6,6]))
