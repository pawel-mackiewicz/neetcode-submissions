class Solution:
    def isValid(self, s: str) -> bool:
        flag = False
        brackets = []
        matches = {'{':'}', '(':')', '[':']'}
        for bracket in s:
            if bracket in {'{', '(', '['}:
                brackets.append(bracket)
                flag = True
            elif len(brackets) > 0:
                last_bracket = brackets.pop()
                if matches[last_bracket] != bracket:
                    return False
            else:
                return False
                

        
        return flag and len(brackets) == 0