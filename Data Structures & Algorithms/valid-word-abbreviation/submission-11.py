class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        # check char by char
        # i, j
        
        i, j = 0, 0

        while i < len(word):
            num = ""
            while j < len(abbr) and abbr[j] in {'1','2','3','4','5','6','7','8','9','0'}:
                num += abbr[j]
                j += 1
                if num == "0":
                    return False
            i += int(num) if num != "" else 0
            if i == len(word) and j == len(abbr):
                return True
            if i > len(word) or (i == len(word) and j < len(abbr)) or (i < len(word) and abbr[j] != word[i]):
                return False
            
            i += 1
            j += 1

        return True