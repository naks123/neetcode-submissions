class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for char in s:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        hashmap2 = {}
        for char in t:
            if char not in hashmap2:
                hashmap2[char] = 1
            else:
                hashmap2[char] += 1
        if hashmap == hashmap2:
            return True
        return False

        
        