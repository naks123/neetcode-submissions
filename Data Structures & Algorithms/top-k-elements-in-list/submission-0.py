class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}
        ans = []
        for num in nums:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        for i in range(k):
            biggest_key = max(hashmap, key=hashmap.get)
            ans.append(biggest_key)
            hashmap.pop(biggest_key)
        return ans