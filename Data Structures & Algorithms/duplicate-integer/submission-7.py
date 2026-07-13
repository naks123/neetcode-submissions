class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        from collections import defaultdict
        unique = set()
        for i in range(len(nums)):
            if nums[i] not in unique:
                unique.add(nums[i])
            else:
                return True
        return False