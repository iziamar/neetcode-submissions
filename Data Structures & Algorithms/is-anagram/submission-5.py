class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dictT, dictS = {}, {}

        for i in range(len(s)):
            dictT[t[i]] = 1 + dictT.get(t[i], 0)
            dictS[s[i]] = 1 + dictS.get(s[i], 0)
        return dictT == dictS
        

        