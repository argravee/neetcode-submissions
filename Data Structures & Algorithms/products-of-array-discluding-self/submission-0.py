class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]
        suffix = [1]
        resulty = []

        for index in range(1, len(nums)):

            result = nums[index-1] * prefix[index-1]
            result2=nums[-index] * suffix[-index]
            prefix.append(result)
            suffix.insert(-index,result2)
        for x,y in zip(prefix,suffix):
            resulty.append(x*y)
        return resulty 



