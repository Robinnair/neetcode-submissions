class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={
            ')':'(',
            ']':'[',
            '}':'{'
        }
        for char in s:
            if char in "{([":
                stack.append(char)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if top!=mapping[char]:
                    return False
        return len(stack)==0