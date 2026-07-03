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
            elif abbr[j] != word[i]:
                return False
            else:
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)