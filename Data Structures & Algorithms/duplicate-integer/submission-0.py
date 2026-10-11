class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        temp = {}
        for i, val in enumerate(nums):
            if val in temp:
                return True
            temp[val] = i
        return False