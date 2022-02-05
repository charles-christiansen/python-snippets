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
print(s.romanToInt("III"))
print(s.romanToInt("LVIII"))
print(s.romanToInt("MCMXCIV"))
