class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0

        substring = ""

        for i,char in enumerate(s):
            if char not in substring:
                substring+= char
                if len(substring) > best:
                    best = len(substring)
            else:
                substring = substring[substring.find(char)+1:]
                substring+=char

        return best
