class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for index, num in enumerate(nums):
            remainder = target-num 
            if remainder in nums[index+1:]:
                return [nums.index(num),nums.index(remainder,index+1)]