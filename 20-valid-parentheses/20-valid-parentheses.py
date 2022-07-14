class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        s_dict = {")": "(", "}": "{", "]": "["}
        for i in s:
            if i in s_dict.values():
                stack.append(i)
            else:
                if len(stack) != 0 and s_dict[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
                
        if len(stack) == 0:
            return True
        else:
            return False