class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = {}
        for i, x in enumerate(nums):
            y = target - x
            if y not in nums_dict:
                nums_dict[x] = i
            else:
                return [nums_dict[y],i]
        return None