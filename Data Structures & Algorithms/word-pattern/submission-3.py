class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        
        if len(pattern) != len(s.split()):
            return False
        wordMap = {}
        seen = set()
        for p,w in zip(pattern,s.split()):
            if p in wordMap:
                if wordMap[p] != w:
                    return False
            elif w not in seen:
                wordMap[p] = w
            else:
                return False
            seen.add(w)
        return True