## Remove Duplicates from Sorted List
## LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array
## Given a list sorted in ascending order, remove all duplicates from the list
## IN PLACE and return the length of the deduped array
## This method seems to be a bit slow, will revisit to optimize
from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=len(nums)-1
        while i > 0:
            while i > 0 and nums[i]==nums[i-1]:
                nums.remove(nums[i-1])
                i-=1
            i-=1
        return len(nums)
s=Solution()
l=[1,2,2,2,2,2,3,3,4,5,5,5,6,6]
print(s.removeDuplicates(l))
