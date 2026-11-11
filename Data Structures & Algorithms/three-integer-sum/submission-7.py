class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i - 1]: 
                continue
            target = 0-num
            l = i+1
            r = len(nums)-1
            while ((l < r) == True):
                if (nums[l]+nums[r] > target):
                    r -= 1
                elif (nums[l]+nums[r] < target):
                    l +=1
                else:
                    out.append([num,nums[l],nums[r]])
                    r-=1
                    l+=1
                    
                    # Skip any more copies of the left value we just used.
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    # Skip any more copies of the right value we just used.
                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1

        return out
                    

        