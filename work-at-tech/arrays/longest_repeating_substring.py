class Solution:
   
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_size = 0
        # Return case of 0 or 1 len string
        if len(s) < 2:
            return len(s)
        ws = 1
        cache = {}
        spt = 0
        for i in range(0,len(s)):
            # Leave if past string end
            if i + ws > len(s):
                break
            # Skip if repeating character that caused problem last time
            elif spt > 0:
                spt -= 1
                continue
            # Set cache
            cache['set'] = None
            save_spt = False
            while True:
                # Set cache
                if cache['set'] is None:
                    cache['set'] = set(s[i:i+ws])
                else:
                    save_spt = True
                    cache['set'].add(s[i+ws-1])
                # Check cache size vs. size of string
                set_size = len(cache['set'])
                if set_size == ws:
                    # Increase window size if no repeats
                    max_size = ws
                    ws+=1
                    if i + ws > len(s):
                        break
                else:
                    # Leave, save problemtic index
                    if save_spt:
                        spt = len(s[i:i+ws].split(s[i+ws-1])[0])
                    break
        return max_size