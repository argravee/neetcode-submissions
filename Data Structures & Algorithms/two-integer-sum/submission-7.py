class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        complement_map = {}
        for index,value in enumerate(nums):
            result = target - value
            if result in complement_map:
                return [complement_map[result],index]
            complement_map[value] = index
