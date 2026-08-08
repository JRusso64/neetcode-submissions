class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closeToOpen = { "(" : ")", "[" : "]", "{" : "}" }

        for paren in s:
            if paren in closeToOpen:
                stack.append(paren)
            else:
                if stack and closeToOpen[stack[-1]] == paren:
                    stack.pop()
                else:
                    return False

        if not stack: 
            return True
        return False