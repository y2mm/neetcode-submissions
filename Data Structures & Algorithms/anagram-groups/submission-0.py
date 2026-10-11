class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tempHash = {}
        anagrams = []
        for i, word in enumerate(strs):
            if tuple(sorted(word))not in tempHash:
                tempHash[tuple(sorted(word))] = [i]
            else:
                tempHash[tuple(sorted(word))].append(i)

        for values in tempHash.values():
            temp = []
            for i in values:
                temp.append(strs[i])
            anagrams.append(temp)
        
        return anagrams
            

            