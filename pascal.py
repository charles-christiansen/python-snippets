## Pascal's triangle
## LeetCode: https://leetcode.com/problems/pascals-triangle
## Given an integer, return the first n rows of Pascal's triangle.
from typing import List
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows==1:
            return [[1]]
        if numRows==2:
            return [[1],[1,1]]

        rows=[[1],[1,1]]
        prevRow=[1,1]
        curRow=[]

        for i in range(3,numRows+1):
            for j in range(0,len(prevRow)+1):
                if j==0 or j==len(prevRow):
                    curRow.append(1)
                else:
                    curRow.append(prevRow[j]+prevRow[j-1])
            rows.append(curRow)
            prevRow=curRow
            curRow=[]
        return rows

s=Solution()
print(s.generate(1))
print(s.generate(2))
print(s.generate(3))
print(s.generate(4))
print(s.generate(5))
