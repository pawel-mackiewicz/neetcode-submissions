class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        orderMap = {}

        for i in range(len(order)):
            orderMap[order[i]] = i

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]

            for j in range(len(w1)):
                if j == len(w2):
                    return False
                l1 = w1[j] 
                l2 = w2[j]
                if orderMap[l1] < orderMap[l2]:
                    break
                if orderMap[l1] > orderMap[l2]:
                    return False
        return True