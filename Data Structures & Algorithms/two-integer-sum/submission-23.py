class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexDict = dict()
        for i in range(len(nums)):
            if (target - nums[i]) in indexDict:
                return [indexDict.get(target - nums[i]), i]
            indexDict[nums[i]] = i
        
        