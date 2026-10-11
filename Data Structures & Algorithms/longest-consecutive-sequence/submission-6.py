class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s = set(nums)
        counter = 1
        maxL = 1
        
        for i, val in enumerate(s):
            if val-1 not in s:
                curr = val
                while curr+1 in s:
                    curr += 1
                    counter += 1
                if maxL < counter:
                    maxL = counter
                counter = 1
        
        return max(maxL,counter)
            
            