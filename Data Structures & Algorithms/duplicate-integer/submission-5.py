class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        myMap = {}
        for i, num in enumerate(nums):
            if num in myMap:
                return True
            myMap[num] = i
        return False
            
        
        