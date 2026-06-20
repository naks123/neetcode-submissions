class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        result = []
        for letter in zip(*strs):
            if len(set(letter)) == 1:
                result.append(letter[0])
            else:
                break
        return "".join(result) 