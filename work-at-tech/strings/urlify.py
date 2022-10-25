input = "Mr. Jones    has no  life      "
output = "Mr.%20Jones%20has%20no%20life"

class Solution:

    space = "%20"

    def urlify(self, s):
        last = True
        new_s = ""
        for i in range(len(s)-1, -1, -1):
            if s[i] == " ":
                if not last:
                    new_s = "%20" + new_s
                    last = True
            else:
                last = False
                new_s = s[i] + new_s
        return output

s = Solution()
assert s.urlify(input) == output