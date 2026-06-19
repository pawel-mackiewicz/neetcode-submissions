class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def dp(amountLeft: int, cache) -> int:
            if amountLeft < 0:
                return amount+1
            if amountLeft == 0:
                return 0
            if amountLeft in cache:
                return cache[amountLeft]
            
            cache[amountLeft] = min(1 + dp(amountLeft - coin, cache) for coin in coins)    
            return cache[amountLeft]

        r = dp(amount, {})
        return r if r <= amount else -1