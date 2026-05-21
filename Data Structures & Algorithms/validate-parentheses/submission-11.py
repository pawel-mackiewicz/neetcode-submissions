class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        matches = {'{':'}', '(':')', '[':']'}
        for bracket in s:
            if bracket in {'{', '(', '['}:
                brackets.append(bracket)
            elif len(brackets) > 0:
                last_bracket = brackets.pop()
                if matches[last_bracket] != bracket:
                    return False
            else:
                return False
        
        return len(brackets) == 0