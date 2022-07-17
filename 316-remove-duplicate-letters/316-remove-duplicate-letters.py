class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        counter = collections.Counter(s)
        stack  = []
        seen = set()
        
        for i in s:
            counter[i] -= 1
            
            # 집합에 i가 있다면
            if i in seen:
                continue
            
            while stack and i < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop()) # 스택에서 지우고 집합에서도 지움
            stack.append(i)
            seen.add(i)
        
        return ''.join(stack)
            