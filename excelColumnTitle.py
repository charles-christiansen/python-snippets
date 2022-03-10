## Excel Sheet Column Title
## LeetCode: https://leetcode.com/problems/excel-sheet-column-title/
## Given an integer columnNumber, return its corresponding column title
## as it appears in an Excel sheet.
## Example: Column 1 = "A", Column 26 = "Z", Column 27 = "AA"
##          Column 52 = "AZ", Column 53 = "BA", Column 702 = "ZZ"
##          Column 703 = "AAA"
## Part of the algorithm can be expressed as follows:
## The single letter titles are columns 26**0 to 26**1
## The double letter titles are columns 26**1 + 26**0 to 26**2 + 26**1.
## The triple letter titles are columns 26**2 + 26**1 + 26**0 to 26**3 + 26**2 + 26**1
## Solve for the title by getting each letter from the list using modulo 26
## Decrement the column number by integer division by 26
## Repeat until the column number is <= 0.
## Because we're appending to the list, it will be in reverse order
## so be sure to reverse it before returning!
import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letterList=list(string.ascii_uppercase)
        title=[]
        while columnNumber > 0:
            title.append(letterList[(columnNumber-1)%26])
            columnNumber = (columnNumber-1)//26
        return ''.join(list(reversed(title)))

s=Solution()
print(s.convertToTitle(1))
print(s.convertToTitle(26))
print(s.convertToTitle(27))
print(s.convertToTitle(52))
print(s.convertToTitle(53))
print(s.convertToTitle(702))
print(s.convertToTitle(703))
print(s.convertToTitle(1239))
