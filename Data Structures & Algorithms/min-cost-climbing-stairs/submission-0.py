class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        ## count from 0 and count from 1 then return min
        cost.append(0)
        def dp(n, cache):
            if n < 2:
                return cost[n]

            if n in cache:
                return cache[n]
            
            cache[n] = cost[n] + min(dp(n-1, cache), dp(n-2, cache))
            return cache[n]
        
        return dp(len(cost)-1, {})

