## Zigzag Conversion
## LeetCode: https://leetcode.com/problems/zigzag-conversion/
## Given a String and a number of rows representing a String
## zigzag, output the String in left to right order
## The zigzag is created by putting each letter of the String
## starting at row 1 column 1 down to row numRows column 1
## then going diagonally back up to row 1 (so column 2, rowNum -1, etc)
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if len(s) <= numRows or numRows==1:
            return s
        numCols=numRows*(len(s)//numRows)
        if len(s)%numRows != 0:
            numCols+=1
        cols=[""]*numCols
        rows=[]
        for n in range(numRows):
            cols=[""]*numCols
            rows.append(cols)
        curRow=0
        curCol=0
        dir=1
        for c in s:
            rows[curRow][curCol]=c
            if curRow >= numRows-1:
                dir=-1
            elif curRow==0:
                dir=1

            if dir==-1:
                curCol+=1
            curRow+=dir
        converted=""
        for row in rows:
            converted+="".join(row)
        return converted

s=Solution()
print(s.convert("PAYPALISHIRING",3))
print(s.convert("PAYPALISHIRING",4))
print(s.convert("A",1))
print(s.convert("Thisismysentence.Itislongerthanprevioussentences,asIamsureyousee.",30))
