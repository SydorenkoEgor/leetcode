class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        l = ""
        i = 0
        while i < len(s):
            if s[i] == ')':
                while len(stack) > 0 and stack[-1] != '(':
                    l += stack.pop()

                if len(stack) > 0:
                    stack.pop()
                for c in l:
                    stack.append(c)
                l = ""
                i += 1
            else:
                stack.append(s[i])
                i += 1
        return "".join(stack)