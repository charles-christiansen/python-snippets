## Two Sum
## LeetCode: https://leetcode.com/problems/two-sum/
## Given a list of numbers and a target value, return a list
## containing the indices of the two numbers in the list which
## add up to the target number. Try to do this in less
## than O(n**2) time complexity
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            n1=nums[i]
            n2=target-n1
            try:
                j=nums.index(n2,i+1)
                return[i,j]
            except:
                continue

s=Solution()
# Return [0,1]
print(s.twoSum([2,7,11,15],9))
# Return [1,2]
print(s.twoSum([3,2,4],6))
# Return [0,1]
print(s.twoSum([3,3],6))
# Return [3,8]
print(s.twoSum([1,3,5,7,9,11,13,15,18,19],25))
