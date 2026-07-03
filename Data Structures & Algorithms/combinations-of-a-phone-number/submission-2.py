class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if len(digits) == 0:
            return []

        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res, curr = [], []

        def helper(start):
            if len(curr) == len(digits):
                res.append(''.join(curr))
                return
            
            digit = digits[start]
            for ch in letters[digit]:
                curr.append(ch)
                helper(start+1)
                curr.pop()
        helper(0)
        return res