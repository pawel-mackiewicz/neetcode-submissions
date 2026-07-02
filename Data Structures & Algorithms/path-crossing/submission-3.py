class Solution:
    def isPathCrossing(self, path: str) -> bool:
        NS = 0
        WE = 0

        pathMap = set()

        for p in path:
            pathMap.add((NS,WE))
            
            if p == "N":
                NS += 1
            elif p == "S":
                NS -= 1
            elif p == "W":
                WE += 1
            elif p == "E":
                WE -= 1
            
            if (NS, WE) in pathMap:
                return True
        return False