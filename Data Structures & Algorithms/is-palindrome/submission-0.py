class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = len(s)-1
        i = 0
        while i in range(0,len(s)):
            if s[i].isalnum():
                if s[j].isalnum():
                    if s[i].lower() != s[j].lower():
                        return False
                    j -= 1
                else:
                    j -= 1
                    i -=1
                
            i += 1
        return True

