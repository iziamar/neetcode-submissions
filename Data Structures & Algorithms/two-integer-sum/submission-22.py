class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        asSeen = {}
        for i, n in enumerate(nums):
            diff = target - n
            if diff in asSeen:
                return [asSeen[diff], i]
            asSeen[n] = i
        
        