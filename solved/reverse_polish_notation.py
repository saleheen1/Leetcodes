from math import ceil,floor

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        
        stk = []

        for v in tokens:
            if v in "+-*/":
                b = int(stk.pop())
                a = int(stk.pop())

                if v == "+":
                    stk.append(a+b)
                elif v == "-":
                    stk.append(a-b)
                elif v == "*":
                    stk.append(a*b)
                else:
                    res = int(float(a)/b)
                    
                    
                    stk.append(res)
            else:
                stk.append(v)
        
        return stk[0]




s =Solution()
print(s.evalRPN(tokens=["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))