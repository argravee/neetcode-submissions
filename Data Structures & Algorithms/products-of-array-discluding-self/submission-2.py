class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        size = len(nums)
        prefix = [1] * size
        suffix = [1] * size
        resulty = []

        for index in range(1, len(nums)):

            result = nums[index-1] * prefix[index-1]
            result2=nums[-index] * suffix[-index]
            prefix[index] = result
            suffix[-index-1]= result2
        for x,y in zip(prefix,suffix):
            resulty.append(x*y)
        return resulty 



