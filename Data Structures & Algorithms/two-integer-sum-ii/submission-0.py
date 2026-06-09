class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        L, R = 0, len(numbers) - 1

        while L < R:
            n1 = numbers[L]
            n2 = numbers[R]

            if n1 + n2 > target:
                R -= 1
            elif n1 + n2 < target:
                L += 1
            else:
                return [L+1,R+1]