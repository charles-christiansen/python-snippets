class Solution:
    def destCity(self, paths: list[list[str]]) -> str:
        dcounts = {}
        for path in paths:
            cityA, cityB = path
            dcounts[cityA]=dcounts.get(cityA,0)+1
            dcounts[cityB]=dcounts.get(cityB,0)
        for dc in dcounts:
            if dcounts[dc]==0:
                return dc
        return None

s = Solution()
print(s.destCity([["B","C"],["D","B"],["C","A"]]))
print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
