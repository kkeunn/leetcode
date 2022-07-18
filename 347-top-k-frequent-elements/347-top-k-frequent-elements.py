class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        result = []
        cnt = 0
        for num, _ in sorted(counter.items(), key = lambda x: (-x[1],x[0])):
                if cnt == k:
                    break
                result.append(num)
                cnt += 1
    
        return result
                