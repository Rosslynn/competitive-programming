class Solution:
    def checkValidString(self, s: str) -> bool:
        op_parentesis = []
        asterisks = []

        for i, char in enumerate(s):
            if char == '(':
               op_parentesis.append(i)
            elif char == ')':
                if op_parentesis:
                    op_parentesis.pop()
                elif asterisks:
                    asterisks.pop()
                else:
                    return False
            elif char == '*':
                asterisks.append(i)

        while op_parentesis and asterisks:
            if asterisks[-1] < op_parentesis[-1]:
                return False

            op_parentesis.pop()
            asterisks.pop()
            
        return not op_parentesis
