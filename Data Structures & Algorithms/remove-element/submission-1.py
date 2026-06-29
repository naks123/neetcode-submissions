class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        for l in range(0, len(nums)):
            if nums[l] != val:
                nums[k] = nums[l]
                k += 1
        return k