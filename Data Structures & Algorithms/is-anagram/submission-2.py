class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        src = {}        

        if (len(s) != len(t)):
            return False

        for ch in s:
            if ch in src:
                src[ch] += 1
            else:
                src[ch] = 1

        for i, ch in enumerate(t):
            if ch in src and src[ch] > 0:
                    src[ch] -= 1
            else:
                return False

        return True
            
        
        