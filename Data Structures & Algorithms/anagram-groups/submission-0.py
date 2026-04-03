from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        temp = defaultdict(list)
        for string in strs:
            sorted_string = "".join(sorted(string, reverse=True))
            temp[sorted_string].append(string)

        result = []
        for value in temp.values():
            result.append(value)

        return result