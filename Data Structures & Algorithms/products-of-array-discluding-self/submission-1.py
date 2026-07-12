class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = 1
        prefix = [1] * size
        suffix = [1] * size
        resulty = []

        for index in range(1, len(nums)):

            result = nums[index-1] * prefix[index-1]
            result2=nums[-index] * suffix[-index]
            prefix.append(result)
            suffix.insert(-index,result2)
        for x,y in zip(prefix,suffix):
            resulty.append(x*y)
        return resulty 



