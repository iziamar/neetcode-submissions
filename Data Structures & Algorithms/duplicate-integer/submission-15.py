class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dic = {}
        for i in range(len(nums)):
            dic[nums[i]] = 1 + dic.get(nums[i], 0)
            if dic[nums[i]] > 1:
                return True
        return False