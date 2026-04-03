class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        sStr = {}
        tStr = {}

        for c in s:
            sStr[c] = sStr.get(c,0) + 1

        for c in t:
            tStr[c] = tStr.get(c,0) + 1

        if sStr == tStr:
            return True

        return False