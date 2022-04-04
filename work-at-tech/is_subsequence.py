class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # Start conditions
        size_t = len(t)
        size_s = len(s)
        if size_t == 0 and size_s == 0:
            return True
        elif size_s == 0:
            return True
        elif size_t == 0 and size_s > 0:
            return False
        # Begin
        t_sub = t
        first = 0
        for i in range(len(s)):
            s_char = s[i]
            if s_char in t_sub:
                ind_of = t_sub.index(s_char) + 1
                t_sub = t_sub[ind_of:]
            else:
                return False
        return True