class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        targetSum = threshold * k
        res = 0
        L = 0
        R = k-1

        currSum = sum(arr[:k-1])
        
        while R < len(arr):
            currSum += arr[R]

            if currSum >= targetSum:
                res += 1

            currSum -= arr[L]
            L += 1
            R += 1
        return res
    