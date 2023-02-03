class Solution:
    def parenthesis_are_valid(self, s: str) -> bool:
        # Matcher
        m = {']' : '[', '}' : '{', ')' : '('}
        # Keep track of parenthesis
        stack = []
        for i in range(len(s)):
            c = s[i]
            # Check if opened new parenthesis
            if c == "{" or c == "[" or c == "(":
                stack.insert(0, c)
            # Check if closing
            elif c == "}" or c == "]" or c == ")":
                # Ensure long enough stack
                if len(stack) < 1:
                    return False
                # Ensure match
                if m[c] == stack[0]:
                    del stack[0]
                else:
                    return False            
        # Check if clean stack or not
        if len(stack) == 0:
            return True
        return False
