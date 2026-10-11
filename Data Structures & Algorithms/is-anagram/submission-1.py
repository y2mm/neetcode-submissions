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
            if ch in src:
                if src[ch] > 0:
                    src[ch] -= 1
                elif src[ch] <= 0: 
                    return False
            elif False == (ch in src):
                return False

        return True
            
        
        