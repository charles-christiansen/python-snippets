class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('(al)','al').replace('()','o')

s = Solution()
print(s.interpret('()()(al)GGG(al)()'))
