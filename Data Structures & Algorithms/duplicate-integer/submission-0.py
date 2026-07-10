from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        uniq = set(nums)
        if len(uniq) < len(nums):
            return True
        return False

        