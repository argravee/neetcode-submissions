class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = {}
        count = {}
        for char in s:
            seen[char] = seen.get(char, 0)+1
        
        for char in t:
            count[char] = count.get(char,0)+1

        if seen == count:
            return True
        return False


        
       
            