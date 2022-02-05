## Goal Parser Interpretation
## LeetCode: https://leetcode.com/problems/goal-parser-interpretation/
## Given a string containing the character sets 'G','()', and '(al)'
## Return a string containing the character sets 'G','o', and 'al'.
class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('(al)','al').replace('()','o')

s = Solution()

# return the string "ooalGGGalo"
print(s.interpret('()()(al)GGG(al)()'))
