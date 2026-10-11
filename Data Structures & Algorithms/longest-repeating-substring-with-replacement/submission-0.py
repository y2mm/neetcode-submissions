class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        temp = {}
        left = 0
        freq = 0
        length = 0
        
        for r, ch in enumerate(s):
            temp[ch] = temp.get(ch, 0) + 1
            freq = max(freq, temp[ch])
            
            while r - left - freq+1 > k:
                temp[s[left]] -= 1
                left += 1
            
            length = max(length, r-left+1)

            
        return length