class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        strs = collections.deque()
        for char in s:
            if char.isalnum(): # 영문자, 숫자 여부 판별
                strs.append(char.lower())
                
        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False
            
        return True