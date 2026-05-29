# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        def binarySearch(low: int, high: int) -> int:
            if low > high:
                pass
            
            middle = (low + high) // 2

            if guess(middle) == -1:
                return binarySearch(low, middle-1)
            if guess(middle) == 1:
                return binarySearch(middle+1, high)
            return middle
        
        return binarySearch(0, n)

            