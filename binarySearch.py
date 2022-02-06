## Binary search
## LeetCode: https://leetcode.com/problems/binary-search/
## Given a sorted list of numbers and a target,
## Return the index of the target in the list.
## Return -1 if the target doesn't appear in the list.
import math
from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lower=0
        upper=len(nums)-1
        while(upper >= lower):
            idx=math.floor((upper+lower)/2)
            if(nums[idx]==target):
                return idx
            elif(nums[idx] < target):
                lower=idx+1
            else:
                upper=idx-1
        return -1

s=Solution()
# return 4
print(s.search([-1,0,3,5,9,12],9))
# return -1
print(s.search([-1,0,3,5,9,12],32))
# return -1
print(s.search([-1,0,3,5,9,12],2))
