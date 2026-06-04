class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        change = {5:0,10:0}
        for bill in bills:
            if bill == 5:
                change[5] += 1
            elif bill == 10:
                if not change[5]:
                    return False
                change[5] -= 1
                change[10] += 1
            elif bill == 20:
                if change[10] and change[5]:
                    change[10] -= 1
                    change[5] -= 1
                elif change[5] >= 3:
                    change[5] -= 3
                else:
                    return False

        return True
        