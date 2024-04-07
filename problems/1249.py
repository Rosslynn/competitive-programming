class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        n = len(s)
        clos = 0
        op = []
        ret = [''] * n

        for i in range(n):
            ret[i] = s[i]
            
            if s[i] == '(':
                op.append(i)
            elif s[i] == ')':
                if len(op) > clos:
                    clos += 1
                else:
                    ret[i] = ''
        
        while len(op) != clos:
            ret[op.pop()] = ''
            
        return ''.join(ret)
