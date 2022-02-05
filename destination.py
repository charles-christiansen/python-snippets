## Final Destination
## LeetCode: https://leetcode.com/problems/destination-city/
## Given a list of lists of origins and destinations,
## Return the final destination.
## The final destination is the one which does not appear
## in any list as an origin.
## The lists are of the format ["Origin","Destination"]
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
# Destintation should be A
print(s.destCity([["B","C"],["D","B"],["C","A"]]))

# Destination should be Sao Paulo
print(s.destCity([["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]))
