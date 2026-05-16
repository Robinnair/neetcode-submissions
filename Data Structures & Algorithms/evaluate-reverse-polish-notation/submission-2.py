class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        for t in tokens:
            if t not in "+*-/":
                stack.append(t)
            else:
                op1=int(stack.pop())
                op2=int(stack.pop())
                if(t=='+'):
                    stack.append(str(op1+op2))
                if(t=='-'):
                    stack.append(str(op2-op1))
                if(t=='*'):
                    stack.append(str(op1*op2))
                if(t=='/'):
                    stack.append(str(int(op2/op1)))
        return int(stack[-1])