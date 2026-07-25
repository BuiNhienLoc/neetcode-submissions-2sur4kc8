class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        
        
        for string in strs:
            value = "".join(sorted(string))

            if value not in groups:
                groups[value]=[]

            groups[value].append(string)
            

        return list(groups.values())