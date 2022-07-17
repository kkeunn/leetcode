class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        result = [0]*len(temperatures)
        for i in range(len(temperatures)):
            # stack에 값이 있고 현재 온도가 이전 온도보다 높으면
            while stack and temperatures[i] > temperatures[stack[-1]]:
                last = stack.pop() # stack에 쌓아둔 index 추출
                result[last] = i - last
                
            stack.append(i)
        
        return result
            
        