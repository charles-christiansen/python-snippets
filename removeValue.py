## Remove Value from List
## LeetCode: https://leetcode.com/problems/remove-element/
## Given a list of ints and a value, remove all instances
## of value from the list IN PLACE and return the length of
## the array
from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        try:
            while True:
                nums.remove(val)
        except:
            return len(nums)

s=Solution()
# return 2
print(s.removeElement([3,2,2,3],3))
# return 5
print(s.removeElement([0,1,2,2,3,0,4,2],2))
# return 7
print(s.removeElement([1,2,3,4,5,6,7],8))
