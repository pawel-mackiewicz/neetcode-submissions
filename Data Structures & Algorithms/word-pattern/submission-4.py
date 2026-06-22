class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        words = s.split()
        if len(pattern) != len(words):
            return False

        wordMap = {}
        seen = set()
        for p,w in zip(pattern,words):
            if p in wordMap:
                if wordMap[p] != w:
                    return False
            elif w not in seen:
                wordMap[p] = w
            else:
                return False
            seen.add(w)
        return True