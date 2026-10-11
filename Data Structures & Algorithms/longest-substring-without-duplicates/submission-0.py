class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        rep = set()
        left = 0

        for i in range(len(s)):
            while s[i] in rep:
                rep.remove(s[left])
                left += 1

            rep.add(s[i])
            if length < len(rep):
                length = len(rep) 

        return length


