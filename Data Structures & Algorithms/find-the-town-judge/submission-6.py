class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trustMap = [0] * (n+1) 

        for a,b in trust:
            trustMap[b] += 1
            trustMap[a] -= 1

        for i in range(1, n+1):
            if trustMap[i] == n-1:
                return i
        
        return -1