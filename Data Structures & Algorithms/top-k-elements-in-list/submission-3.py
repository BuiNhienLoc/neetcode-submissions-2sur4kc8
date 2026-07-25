class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}

        for num in nums:
            if num not in dictionary: dictionary[num]=0
            dictionary[num]+=1

        return sorted(dictionary, key=dictionary.get, reverse=True)[:k]        