class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0

        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                num = ""
                while j < len(abbr) and abbr[j].isdigit():
                    num += abbr[j]
                    if num == "0":
                        return False
                    j += 1
                i += int(num) if num != "" else 0
                i -= 1
                j -= 1
            elif abbr[j] != word[i]:
                return False
            
            i += 1
            j += 1

        if i == len(word) and j == len(abbr):
            return True
        return False