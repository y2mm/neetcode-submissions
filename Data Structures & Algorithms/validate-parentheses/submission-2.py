class Solution:
    def isValid(self, s: str) -> bool:
        stck = []
        paran = {')':'(', '}':'{', ']':'['}


        for ch in s:
            if ch in paran:
                if not stck or stck[-1] != paran[ch]:
                    return False
                else:
                    stck.pop()
            else:
                stck.append(ch)
        
        return not stck

        