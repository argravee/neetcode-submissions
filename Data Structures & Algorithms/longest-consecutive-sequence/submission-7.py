class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        s = sorted(set(nums))
        result = 1
        best = 1
        for index, value in enumerate(s[:-1]):
            if s[index + 1] == value + 1:
                result += 1

            if result > best:
                best = result

            if s[index + 1] != value + 1:
                result = 1

        return best
