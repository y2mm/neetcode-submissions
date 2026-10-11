class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        m = l + r //2

        if nums[l] < nums[m] < nums[r]:
            return nums[l]
            
        while l < r:
            m = (l + r) //2
            if nums[m]>nums[r]:
                l = m+1
            else:
                r=m
            
        return nums[l]