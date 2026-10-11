class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        numbers = sorted(nums)
        answers = set()

        for i, num in enumerate(numbers):
            l = i+1
            r = len(numbers)-1
            while l < r:
                if numbers[l]+numbers[r]+numbers[i]>0:
                    r -=1
                elif numbers[l]+numbers[r]+numbers[i]<0:
                    l +=1
                else:
                    answers.add(tuple(sorted([numbers[l],numbers[r],numbers[i]])))
                    r -=1
                    l +=1
                    
        return list(answers)