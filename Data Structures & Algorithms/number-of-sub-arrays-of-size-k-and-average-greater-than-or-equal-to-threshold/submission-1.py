class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        res = 0
        L = 0
        R = k-1

        currSum = sum(arr[0:k-1])

        while R < len(arr):
            currSum = currSum + arr[R]

            if currSum / k >= threshold:
                res += 1
            currSum = currSum - arr[L]
            L += 1
            R += 1
        return res