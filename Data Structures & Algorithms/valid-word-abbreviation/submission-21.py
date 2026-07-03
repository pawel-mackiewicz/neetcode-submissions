class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word):
            num = ""
            while j < len(abbr) and abbr[j].isdigit():
                num += abbr[j]
                if num == "0":
                    return False
                j += 1
            i += int(num) if num != "" else 0
            
            if i == len(word) and j == len(abbr):
                return True
            if i >= len(word) or (j >= len(abbr) and i < len(word)) or (j < len(abbr) and abbr[j] != word[i]):
                return False
            
            i += 1
            j += 1

        return True