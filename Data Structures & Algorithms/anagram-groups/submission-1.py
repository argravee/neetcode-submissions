class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hm = {}
        for value in strs:
            key = "".join(sorted(value))
            if key in hm:
                hm[key].append(value)
            else:
                hm[key] = [value]
        return list(hm.values())