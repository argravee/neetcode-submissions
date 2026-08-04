class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm={}
        for index,value in enumerate(nums):
            result = target - value 
            if result in hm:
                return [hm[result],index]
            hm[value] = index
