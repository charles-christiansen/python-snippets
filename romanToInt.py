## Roman to Integer
## LeetCode: https://leetcode.com/problems/roman-to-integer/
## Given a valid Roman numeral string consisting of characters
## I,V,X,L,C,D, and M
## Return the integer value
class Solution:
    def romanToInt(self, s: str) -> int:
        romNums={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        num=0
        for i in range(len(s)):
            if i > 0 and romNums[s[i]] > romNums[s[i-1]]:
                num+=romNums[s[i]] - romNums[s[i-1]]*2
            else:
                num+=romNums[s[i]]
        return num

s=Solution()
# 3
print(s.romanToInt("III"))
# 58
print(s.romanToInt("LVIII"))
# 1994
print(s.romanToInt("MCMXCIV"))
