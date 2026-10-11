class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        lens1 = len(s1)

        if lens1 > len(s2):
            return False

        s1count = Counter(s1)
        s2count = Counter(s2[:lens1])

        for i in range(0, len(s2) - lens1):
            if s2count == s1count:
                return True
            else:
                s2count[s2[i]] -= 1
                s2count[s2[i + lens1]] += 1

        return s2count == s1count