class Solution:
    def makeGood(self, s: str) -> str:
        stack = []

        for char in s:
            curr = ord(char)
            peek = stack and ord(stack[-1])

            if (curr + 32) == peek or (curr - 32) == peek:
                stack.pop()
                continue
            
            stack.append(char)

        return ''.join(stack)