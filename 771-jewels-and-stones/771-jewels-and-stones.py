class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        counter = collections.Counter(stones)
        
        cnt = 0
        for jewel in jewels:
            cnt += counter[jewel]
        
        return cnt