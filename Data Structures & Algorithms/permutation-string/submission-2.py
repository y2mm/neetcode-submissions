class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1 = len(s1)
        if lens1>len(s2):
            return False
        x = sorted(s1)

        for i in range(0,len(s2)-lens1+1):
            if sorted(s2[i:i+lens1]) == x:
                return True

        return False