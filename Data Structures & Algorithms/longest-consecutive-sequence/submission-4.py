class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        nums.sort()
        counter = 1
        maxL = 1


        for i, val in enumerate(nums):
            if i < len(nums)-1:
                if val == nums[i+1]:
                    continue
                if val+1 == nums[i+1]:
                    counter += 1
                else:
                    if maxL < counter:
                        maxL = counter
                    counter = 1
        

        return max(maxL,counter)
            