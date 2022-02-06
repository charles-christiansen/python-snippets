## Valid Parentheses
## LeetCode: https://leetcode.com/problems/valid-parentheses/
## Given a list of numbers and a target value, return a list
## containing the indices of the two numbers in the list which
## add up to the target number. Try to do this in less
## than O(n**2) time complexity
class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 != 0:
            return False
        openers=["(","{","["]
        closers=[")","}","]"]
        openStack=[]
        closeStack=[]
        for c in s:
            try:
                idx=openers.index(c)
                openStack.append(c)
                closeStack.insert(0,closers[idx])
            except:
                idx=closers.index(c)
                if len(closeStack)==0 or c != closeStack[0]:
                    return False
                openStack.pop()
                closeStack.pop(0)
        if len(openStack) > 0 or len(closeStack) > 0:
            return False

        return True

s=Solution()
print(s.isValid("()"))
print(s.isValid("()[]{}"))
print(s.isValid("(]"))
print(s.isValid("({}])"))
print(s.isValid("("))
print(s.isValid("(())"))
