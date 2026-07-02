class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        left = len(digits) - 1
        while left >= 0:
            if digits[left] == 9:
                digits[left] = 0
                left -= 1
            else:
                digits[left] += 1
                break
        if left < 0:
            digits.insert(0, 1)
        return digits