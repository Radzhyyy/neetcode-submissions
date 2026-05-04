class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)

        for word in strs:
            newlist = [0] * 26
            
            for letter in word:
                newlist[ord(letter) - ord('a')] += 1
            
            hashmap[tuple(newlist)].append(word)
        
        return list(hashmap.values())


  