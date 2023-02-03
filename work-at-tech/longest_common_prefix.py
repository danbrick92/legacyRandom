class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        best = ""
        for i in range(len(strs[0])+1):
            prefix = strs[0][0:i]
            for string in strs:
                if string[0:i] != prefix:
                    return best
            best = prefix
        return best