## Pascal's triangle row selection
## LeetCode: https://leetcode.com/problems/pascals-triangle-ii
## Given an integer, return the 0-indexed row of Pascal's triangle
## represented by that integer.
from typing import List
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row=[1]
        prev=1
        for i in range(1,rowIndex+1):
            next=prev*(rowIndex-i+1)//i
            row.append(next)
            prev=next
        return row

s=Solution()
print(s.getRow(0))
print(s.getRow(1))
print(s.getRow(2))
print(s.getRow(3))
print(s.getRow(4))
print(s.getRow(5))
