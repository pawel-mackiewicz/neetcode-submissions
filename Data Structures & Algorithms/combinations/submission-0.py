class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        currSet, res = [], []

        def helper(start):
            if len(currSet) == k:
                res.append(currSet.copy())
                return


            for i in range(start, n+1):
                currSet.append(i)
                helper(i+1)
                currSet.pop()

        helper(1)

        return res