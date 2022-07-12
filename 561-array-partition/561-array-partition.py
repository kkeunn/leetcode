class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        odd_list = nums[::2]
        
        return sum(odd_list)